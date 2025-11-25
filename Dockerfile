# Dockerfile
# Phoenix-Evasion-Research Framework 2025
# Author: QurolVoV (100% solo developer)

# ===== LINUX BASE (untuk CI & runtime ringan) =====
FROM python:3.11-slim-bookworm AS linux-base
LABEL maintainer="QurolVoV"
LABEL org.opencontainers.image.source="https://github.com/QurolVoV/phoenix-evasion-research"

# Install dependencies sistem (untuk psutil, dll)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install -e .

# ===== WINDOWS BASE (untuk Windows runner & research) =====
FROM mcr.microsoft.com/windows/servercore:ltsc2019-amd64 AS windows-base
SHELL ["powershell", "-Command"]

RUN Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe -OutFile python.exe; \
    Start-Process python.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait; \
    Remove-Item python.exe

ENV PATH="${PATH};C:\Python311;C:\Python311\Scripts"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install -e .

# ===== FINAL IMAGE (Linux — default untuk produksi) =====
FROM linux-base AS final
ENTRYPOINT ["python", "-m", "phoenix_evasion_research"]
CMD ["--help"]
