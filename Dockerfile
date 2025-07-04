FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY uv.lock .
COPY src/ .


# RUN uv add "mcp[cli]"
# RUN uv sync --locked

# Install dependencies using uv
RUN uv venv && \
    uv pip install "mcp[cli]" && \
    uv sync --locked

# Ensure venv binaries are available in PATH
ENV PATH="/app/.venv/bin:$PATH"


EXPOSE 8000

CMD ["python", "server.py"]