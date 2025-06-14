# Typst MCP Server

A Model Context Protocol (MCP) server that provides Typst documentation to Claude Code and other MCP clients.

## Installation

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Install as a package

```bash
uv add --dev typst-mcp
```

## Quickstart

### 1. Add to Claude Code configuration

Run the following command to add the Typst MCP server to your project-scope Claude Code configuration:

```bash
claude mcp add typst -s project uvx  
```

Or manually add it to your `.mcp.json` configuration file:

```json
{
  "mcpServers": {
    "typst": {
      "command": "uv",
      "args": ["run", "typst-mcp"],
    }
  }
}
```

### 2. Start using Typst capabilities

Once configured, you can ask Claude Code to help you with Typst documentation. For example:

```
Add a Tabel of Contents to index.typ
```

```
Explain this Typst syntax: #set page(paper: "a4", margin: 2cm)
```

## Documentation

### Tools

#### `typst_search`
Search through Typst documentation for specific topics, functions, or syntax.

**Parameters:**
- `query` (string): Search term or phrase to find in Typst documentation

**Returns:** List of relevant documentation sections with titles, descriptions, and file paths.

**Example:**
```json
{
  "name": "typst_search",
  "arguments": {
    "query": "table formatting"
  }
}
```

#### `typst_browse`
Browse the Typst documentation structure as a hierarchical tree.

**Parameters:**
- `depth` (integer, optional): Maximum depth to traverse (default: 0 for full depth)
- `sub_directory` (string, optional): Subdirectory to explore (default: "." for root)

**Returns:** Tree structure of documentation files and directories.

**Example:**
```json
{
  "name": "typst_browse",
  "arguments": {
    "depth": 2,
    "sub_directory": "reference"
  }
}
```

#### `typst_read`
Read the content of a specific Typst documentation file.

**Parameters:**
- `path` (string): Relative path to the documentation file

**Returns:** Full content of the specified documentation file in markdown format.

**Example:**
```json
{
  "name": "typst_read",
  "arguments": {
    "path": "reference/layout/table.md"
  }
}
```

### Development

#### Setting up development environment

```bash
git clone https://github.com/FujishigeTemma/typst-mcp.git
cd typst-mcp
uv sync --dev
```

#### Running tests

```bash
uv run --frozen pytest
```

#### Code formatting

```bash
uv run --frozen ruff format .
uv run --frozen ruff check . --fix
```

#### Type checking

```bash
uv run --frozen ty
```

### License

MIT License - see LICENSE file for details.

### Related Projects

- [Typst](https://typst.app/) - The Typst typesetting system
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Model Context Protocol SDK for Python
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - AI-powered coding assistant