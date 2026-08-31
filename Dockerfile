FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install the package and dependencies
RUN pip install --no-cache-dir .

# Entry point for running MCP via stdio
ENTRYPOINT ["python", "-m", "joke_mcp"]
