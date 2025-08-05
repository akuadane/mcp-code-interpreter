FROM python:3.10-slim-buster

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY uv.lock .
COPY src/ .

# Install dependencies using uv
RUN uv venv && \
    uv sync --locked

# Ensure venv binaries are available in PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["python", "server.py"]