# ---------- Build stage ----------
FROM python:3.13-slim-bookworm AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv venv --python 3.13 /opt/venv && \
    uv sync --frozen --no-dev

# ---------- Runtime stage ----------
FROM python:3.13-slim-bookworm

WORKDIR /app

# Install build dependencies if needed
RUN apt-get update && apt-get install -y build-essential

# Create virtual environment
RUN python -m venv /opt/venv

# Upgrade pip
RUN /opt/venv/bin/pip install --upgrade pip

# Copy project files
COPY pyproject.toml .
COPY . .

# Copy start.sh and make it executable
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Install dependencies
RUN /opt/venv/bin/pip install .

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 9000

CMD ["/start.sh"]
