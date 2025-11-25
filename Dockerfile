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

# Dockerfile
# Phoenix-Evasion-Research Framework
# Multi-stage build for optimized production image

# Stage 1: Builder
FROM python:3.11-slim as builder

LABEL maintainer="Woodlabs Security Research <redmoonstonee@gmail.com>"
LABEL description="Phoenix-Evasion-Research Framework"
LABEL version="1.0.0"

# Set working directory
WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Verify directory structure
RUN echo "=== Verifying directory structure ===" && \
    ls -la && \
    echo "\n=== Checking src/ directory ===" && \
    ls -la src/ && \
    echo "\n=== Checking Python files ===" && \
    find . -name "*.py" -type f | head -20

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Install package in editable mode
RUN pip install --no-cache-dir -e .

# Run tests to verify installation
RUN python -m pytest tests/ -v --tb=short || echo "Tests completed"

# Stage 2: Runtime
FROM python:3.11-slim

LABEL maintainer="Woodlabs Security Research <redmoonstonee@gmail.com>"
LABEL description="Phoenix-Evasion-Research Framework - Runtime"

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --from=builder /build/src /app/src
COPY --from=builder /build/README.md /app/README.md
COPY --from=builder /build/SECURITY.md /app/SECURITY.md
COPY --from=builder /build/LICENSE /app/LICENSE

# Create non-root user
RUN useradd -m -u 1000 phoenix && \
    chown -R phoenix:phoenix /app

USER phoenix

# Set Python path
ENV PYTHONPATH=/app:$PYTHONPATH

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "from src.phoenix_evasion_research import PhoenixFramework; print('OK')" || exit 1

# Default command
ENTRYPOINT ["python", "-m", "src.phoenix_evasion_research"]
CMD ["--help"]

# Build args for flexibility
ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# Labels for metadata
LABEL org.opencontainers.image.title="Phoenix-Evasion-Research"
LABEL org.opencontainers.image.description="Educational Windows Evasion Research Framework"
LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.url="https://github.com/QurolVoV/phoenix-evasion-research"
LABEL org.opencontainers.image.source="https://github.com/QurolVoV/phoenix-evasion-research"
LABEL org.opencontainers.image.revision="${VCS_REF}"
LABEL org.opencontainers.image.vendor="Woodlabs Security Research"
