# Joke Generator MCP

A simple Model Context Protocol (MCP) server built with Python that provides developer and programming jokes.

## Objective
This project is built as part of an MCP learning workflow to understand how MCP servers are structured, tested, and deployed.

## Features
- **Tools**:
  - `get_random_joke`: Returns a random developer joke.
  - `get_joke_by_topic`: Returns a joke based on a specific programming topic (e.g., Python, JavaScript, CSS).

## Setup & Installation

1. **Clone or Download the Repository**
2. **Install Dependencies:**
   Ensure you have Python 3.10+ installed. Install the package locally:
   ```bash
   pip install -e .
   ```

## Usage (Local Testing)

You can run the MCP server directly using stdio:
```bash
python -m joke_mcp
```

### Testing with the MCP Inspector
To interactively test the server, use the official MCP Inspector:
```bash
npx @modelcontextprotocol/inspector python -m joke_mcp
```
This will start a local web interface where you can invoke the tools provided by this server.

## Deployment to Smithery
This project includes a `smithery.yaml` configuration file for easy deployment to the [Smithery](https://smithery.ai) marketplace.

1. Ensure your code is hosted on a public GitHub repository.
2. Go to Smithery and click "Add Server".
3. Provide your repository URL. Smithery will read the `smithery.yaml` and configure the build automatically.

## Learning Outcomes
- Demonstrated how to use the `mcp` Python SDK to create tools.
- Set up a standard Python package structure.
- Prepared for public sharing via an MCP marketplace.
