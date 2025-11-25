# ================================
# Phoenix-Evasion-Research 2025
# Multi-platform Docker Build
# GitHub: https://github.com/QurolVoV/Phoenix-Evasion-Research
# ================================

# ===== STAGE 1: Linux Base (Default & CI) =====
FROM python:3.11-slim-bookworm AS linux-base

LABEL maintainer="QurolVoV"
LABEL org.opencontainers.image.title="Phoenix Evasion Research"
LABEL org.opencontainers.image.source="https://github.com/QurolVoV/Phoenix-Evasion-Research"
LABEL org.opencontainers.image.description="Educational Evasion Research Framework"

# Install build dependencies (untuk psutil, cryptography, dll)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy hanya yang dibutuhkan (biar layer bisa di-cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code (hanya src/ & file penting)
COPY src/ ./src/
COPY pyproject.toml README.md LICENSE ./

# Install package in editable mode (jika pakai pyproject.toml)
RUN pip install -e .

# ===== STAGE 2: Windows Base (untuk Windows CI & research) =====
FROM mcr.microsoft.com/windows/servercore:ltsc2019-amd64 AS windows-base

# Install Python 3.11
SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe -OutFile python.exe -UseBasicParsing; \
    Start-Process python.exe -ArgumentList '/quiet', 'InstallAllUsers=1', 'PrependPath=1', 'Include_pip=1' -Wait; \
    Remove-Item python.exe -Force

ENV PATH="C:\Python311;C:\Python311\Scripts;${PATH}"

WORKDIR /app

# Copy & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source
COPY src/ ./src/
COPY pyproject.toml README.md LICENSE ./

RUN pip install -e .

# ===== FINAL IMAGE: Linux (default) =====
FROM linux-base AS final-linux
ENTRYPOINT ["python", "-m", "src.phoenix_evasion_research"]
CMD ["--help"]

# ===== FINAL IMAGE: Windows =====
FROM windows-base AS final-windows
ENTRYPOINT ["python.exe", "-m", "src.phoenix_evasion_research"]
CMD ["--help"]

# Default target = Linux (paling sering dipakai)
FROM final-linux
