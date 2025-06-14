"""Typst MCP Server implementation."""

import pathlib
from typing import Any

from mcp.server import Server
from mcp.types import TextContent, Tool


class TypstDocumentationServer:
    """MCP server for Typst documentation."""

    def __init__(self, docs_path: pathlib.Path) -> None:
        self.server = Server("typst-mcp")
        self.docs_path = docs_path
        self._setup_tools()
        self._setup_handlers()

    def _setup_tools(self) -> None:
        """Register available tools."""

        @self.server.list_tools()
        async def handle_list_tools() -> list[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="typst_search",
                    description="Search through Typst documentation for specific topics, functions, or syntax",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search term or phrase to find in Typst documentation",
                            }
                        },
                        "required": ["query"],
                    },
                ),
                Tool(
                    name="typst_browse",
                    description="Browse the Typst documentation structure as a hierarchical tree",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "depth": {
                                "type": "integer",
                                "description": "Maximum depth to traverse (default: 0 for full depth)",
                                "default": 0,
                            },
                            "sub_directory": {
                                "type": "string",
                                "description": "Subdirectory to explore (default: '.' for root)",
                                "default": ".",
                            },
                        },
                    },
                ),
                Tool(
                    name="typst_read",
                    description="Read the content of a specific Typst documentation file",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string",
                                "description": "Relative path to the documentation file",
                            }
                        },
                        "required": ["path"],
                    },
                ),
            ]

    def _setup_handlers(self) -> None:
        """Setup tool call handlers."""

        @self.server.call_tool()
        async def handle_call_tool(
            name: str, arguments: dict[str, Any]
        ) -> list[TextContent]:
            """Handle tool calls."""
            if name == "typst_search":
                return await self._handle_search(arguments["query"])
            elif name == "typst_browse":
                depth = arguments.get("depth", 0)
                sub_directory = arguments.get("sub_directory", ".")
                return await self._handle_browse(depth, sub_directory)
            elif name == "typst_read":
                return await self._handle_read(arguments["path"])
            else:
                raise ValueError(f"Unknown tool: {name}")

    async def _handle_search(self, query: str) -> list[TextContent]:
        """Handle search requests."""
        results = []
        search_term = query.lower()

        # Search through documentation files
        for file_path in self._find_markdown_files():
            try:
                content = file_path.read_text(encoding="utf-8")
                lines = content.split("\n")

                # Search in content
                matches = []
                for i, line in enumerate(lines):
                    if search_term in line.lower():
                        # Get context around the match
                        start = max(0, i - 2)
                        end = min(len(lines), i + 3)
                        context = "\n".join(lines[start:end])
                        matches.append({"line": i + 1, "context": context})

                if matches:
                    relative_path = file_path.relative_to(self.docs_path)
                    results.append(
                        {
                            "file": str(relative_path),
                            "matches": matches[:3],  # Limit to first 3 matches per file
                        }
                    )

            except Exception:
                continue  # Skip files that can't be read

        # Format results
        if not results:
            return [
                TextContent(type="text", text=f"No results found for query: {query}")
            ]

        result_text = f"Search results for '{query}':\n\n"
        for result in results[:10]:  # Limit to first 10 files
            result_text += f"📄 **{result['file']}**\n"
            for match in result["matches"]:
                result_text += f"  Line {match['line']}:\n"
                result_text += f"  ```\n{match['context']}\n  ```\n\n"

        return [TextContent(type="text", text=result_text)]

    async def _handle_browse(self, depth: int, sub_directory: str) -> list[TextContent]:
        """Handle browse requests."""
        target_path = (
            self.docs_path / sub_directory if sub_directory != "." else self.docs_path
        )

        if not target_path.exists():
            return [
                TextContent(type="text", text=f"Directory not found: {sub_directory}")
            ]

        tree_text = f"📁 Directory structure for: {sub_directory}\n\n"
        tree_text += self._generate_tree(target_path, depth, 0)

        return [TextContent(type="text", text=tree_text)]

    async def _handle_read(self, path: str) -> list[TextContent]:
        """Handle read requests."""
        file_path = self.docs_path / path

        if not file_path.exists():
            return [TextContent(type="text", text=f"File not found: {path}")]

        if not file_path.is_file():
            return [TextContent(type="text", text=f"Path is not a file: {path}")]

        try:
            content = file_path.read_text(encoding="utf-8")
            return [TextContent(type="text", text=f"📄 **{path}**\n\n{content}")]
        except Exception as e:
            return [
                TextContent(type="text", text=f"Error reading file {path}: {str(e)}")
            ]

    def _find_markdown_files(self) -> list[pathlib.Path]:
        """Find all markdown files in the documentation directory."""
        if not self.docs_path.exists():
            return []

        return list(self.docs_path.rglob("*.md"))

    def _generate_tree(
        self, path: pathlib.Path, max_depth: int, current_depth: int
    ) -> str:
        """Generate a tree structure of the directory."""
        if max_depth > 0 and current_depth >= max_depth:
            return ""

        tree = ""
        indent = "  " * current_depth

        try:
            items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

            for item in items:
                if item.is_dir():
                    tree += f"{indent}📁 {item.name}/\n"
                    if max_depth == 0 or current_depth < max_depth - 1:
                        tree += self._generate_tree(item, max_depth, current_depth + 1)
                else:
                    icon = "📄" if item.suffix == ".md" else "📋"
                    tree += f"{indent}{icon} {item.name}\n"
        except PermissionError:
            tree += f"{indent}❌ Permission denied\n"

        return tree
