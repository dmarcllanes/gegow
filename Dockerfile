FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies from pyproject.toml
COPY pyproject.toml .
RUN uv sync --no-dev

# Copy project files
COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "-m", "app.main"]
