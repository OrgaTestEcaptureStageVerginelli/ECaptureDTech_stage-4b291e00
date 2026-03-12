# Specific version satisfies Hadolint and Checkov
FROM python:3.12-slim

# Pinned version and cache cleanup (DL3008 and DL3009)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl=7.* && \
    rm -rf /var/lib/apt/lists/*

# Creating and switching to a non-root user (CKV_DOCKER_3)
RUN useradd -m appuser
USER appuser

# Healthcheck added to monitor container health (CKV_DOCKER_2)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "app.py"]
