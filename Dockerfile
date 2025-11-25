# ================================
# Phoenix-Evasion-Research 2025
# Optimized Docker Build
# GitHub: https://github.com/QurolVoV/Phoenix-Evasion-Research
# ================================

FROM python:3.11-slim-bookworm

LABEL maintainer="QurolVoV"
LABEL org.opencontainers.image.title="Phoenix Evasion Research"
LABEL org.opencontainers.image.source="https://github.com/QurolVoV/Phoenix-Evasion-Research"
LABEL org.opencontainers.image.description="Educational Evasion Research Framework"

# Install build dependencies (untuk psutil, cryptography, dll)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Copy requirements first untuk optimal caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy source code dan dokumentasi
COPY src/ ./src/

# Copy package files (gunakan conditional approach)
COPY pyproject.toml LICENSE ./

# Conditional copy untuk README.md - buat fallback jika tidak ada
RUN if [ -f README.md ]; then \
        echo "README.md found, copying..."; \
        cp README.md .; \
    else \
        echo "README.md not found, creating placeholder..."; \
        echo "# Phoenix-Evasion-Research Framework" > README.md; \
        echo "Educational Evasion Research Framework" >> README.md; \
    fi

# Install package in editable mode
RUN pip install -e .

# Cleanup build dependencies untuk mengurangi image size
RUN apt-get purge -y --auto-remove gcc g++ python3-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Set entrypoint
ENTRYPOINT ["python", "-m", "src.phoenix_evasion_research"]
CMD ["--help"]
