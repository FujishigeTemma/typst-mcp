"""CLI interface for the Typst MCP Server."""

import pathlib

import anyio
import click
import uvicorn
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from mcp.server.stdio import stdio_server
from starlette.applications import Starlette
from starlette.routing import Mount

from .server import TypstDocumentationServer

TYPST_VERSION = "v0.13.1"


def get_default_docs_path() -> pathlib.Path:
    """Get the default documentation path based on TYPST_VERSION."""
    return pathlib.Path(__file__).parent.parent.parent / TYPST_VERSION


@click.group()
@click.version_option()
def cli() -> None:
    """Typst MCP Server - A Model Context Protocol server for Typst documentation.

    This CLI provides commands to interact with Typst documentation,
    including search, browse, and read operations.
    """
    pass


@cli.command()
@click.argument("transport", type=click.Choice(["stdio", "http"]), default="stdio")
@click.option(
    "--port",
    type=int,
    default=8000,
    help="Port to bind the HTTP server to (default: 8000, only used with 'http' transport)",
)
@click.option(
    "--host",
    default="127.0.0.1",
    help="Host to bind the HTTP server to (default: 127.0.0.1, only used with 'http' transport)",
)
@click.option(
    "--docs-path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=pathlib.Path
    ),
    help=f"Path to Typst documentation directory (default: {TYPST_VERSION} in project root)",
)
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug mode with additional logging",
)
def serve(
    transport: str,
    port: int,
    host: str,
    docs_path: pathlib.Path | None,
    debug: bool,
) -> None:
    """Start the MCP server with specified transport.

    TRANSPORT: Choose between 'stdio' (default, MCP standard) or 'http' (Streamable HTTP)

    - stdio: Standard MCP communication via stdin/stdout
    - http: HTTP server with Streamable HTTP for web-based clients
    """
    if debug:
        click.echo("Debug mode enabled")

    actual_docs_path = docs_path if docs_path else get_default_docs_path()
    server_instance = TypstDocumentationServer(actual_docs_path)

    if docs_path:
        click.echo(f"Using custom documentation path: {docs_path}")
    else:
        click.echo(f"Using default documentation path: {TYPST_VERSION}/")

    click.echo("\nAvailable tools:")
    click.echo("  • typst_search - Search through documentation")
    click.echo("  • typst_browse - Browse directory structure")
    click.echo("  • typst_read - Read specific documentation files")

    if transport == "http":
        click.echo(f"\nStarting HTTP server on http://{host}:{port}")
        click.echo("Available endpoints:")
        click.echo(f"  • HTTP  http://{host}:{port}/mcp - MCP over HTTP endpoint")

        session_manager = StreamableHTTPSessionManager(
            app=server_instance.server,
            event_store=None,
            json_response=True,
            stateless=True,
        )

        async def handle_streamable_http(scope, receive, send):
            await session_manager.handle_request(scope, receive, send)

        starlette_app = Starlette(
            debug=debug,
            routes=[
                Mount("/mcp", app=handle_streamable_http),
            ],
        )

        uvicorn.run(starlette_app, host=host, port=port)
    else:  # stdio
        click.echo("\nStarting Typst MCP Server...")
        click.echo("Server will communicate via stdio (MCP standard)")
        click.echo("Server ready. Waiting for MCP client connection...")

        async def async_main() -> None:
            async with stdio_server() as (read_stream, write_stream):
                await server_instance.server.run(
                    read_stream,
                    write_stream,
                    server_instance.server.create_initialization_options(),
                )

        anyio.run(async_main)


@click.group()
def tools() -> None:
    """MCP tools for interacting with Typst documentation."""
    pass


@tools.command("list")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "json", "table"]),
    default="table",
    help="Output format (default: table)",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show detailed information about each tool including schemas and examples",
)
def list_tools(output_format: str, verbose: bool) -> None:
    """List all available MCP tools provided by the server.

    Shows the tools that can be used by MCP clients when connecting
    to this server, including their descriptions, input/output schemas,
    and usage examples.
    """

    async def run_tools() -> None:
        # Get tools from the server (simulate the list_tools call)
        tools_data = [
            {
                "name": "typst_search",
                "description": f"Search through Typst {TYPST_VERSION} documentation for specific topics, functions, or syntax",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search term or phrase to find in Typst documentation",
                        }
                    },
                    "required": ["query"],
                },
                "output_schema": {
                    "type": "object",
                    "description": "Returns search results with file locations and contextual matches",
                    "properties": {
                        "type": {"type": "string", "enum": ["text"]},
                        "text": {
                            "type": "string",
                            "description": "Formatted search results with file names, line numbers, and context",
                        },
                    },
                },
                "examples": [
                    {
                        "description": "Search for function definitions",
                        "input": {"query": "function"},
                        "usage": "Find all function-related documentation",
                    },
                    {
                        "description": "Search for specific syntax",
                        "input": {"query": "let variable"},
                        "usage": "Find variable declaration syntax",
                    },
                ],
            },
            {
                "name": "typst_browse",
                "description": "Browse the Typst documentation structure as a hierarchical tree",
                "input_schema": {
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
                "output_schema": {
                    "type": "object",
                    "description": "Returns hierarchical directory structure with files and folders",
                    "properties": {
                        "type": {"type": "string", "enum": ["text"]},
                        "text": {
                            "type": "string",
                            "description": "Tree-structured directory listing with emojis for files and folders",
                        },
                    },
                },
                "examples": [
                    {
                        "description": "Browse root directory",
                        "input": {},
                        "usage": "Get overview of entire documentation structure",
                    },
                    {
                        "description": "Browse specific subdirectory with depth limit",
                        "input": {"sub_directory": "reference", "depth": 2},
                        "usage": "Explore reference section with limited depth",
                    },
                ],
            },
            {
                "name": "typst_read",
                "description": "Read the content of a specific Typst documentation file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the documentation file",
                        }
                    },
                    "required": ["path"],
                },
                "output_schema": {
                    "type": "object",
                    "description": "Returns the complete content of the specified documentation file",
                    "properties": {
                        "type": {"type": "string", "enum": ["text"]},
                        "text": {
                            "type": "string",
                            "description": "Full file content with filename header",
                        },
                    },
                },
                "examples": [
                    {
                        "description": "Read a specific function documentation",
                        "input": {"path": "reference/foundations/calc.md"},
                        "usage": "Get detailed documentation for calc module",
                    },
                    {
                        "description": "Read tutorial file",
                        "input": {"path": "tutorial/writing-in-typst.md"},
                        "usage": "Learn about writing content in Typst",
                    },
                ],
            },
        ]

        if output_format == "json":
            import json

            click.echo(json.dumps(tools_data, indent=2))
        elif output_format == "table":
            click.echo("Available MCP Tools")
            click.echo("=" * 80)
            click.echo()

            for tool in tools_data:
                click.echo(f"🔧 {tool['name']}")
                click.echo(f"   {tool['description']}")
                click.echo()

                if verbose:
                    # Input Schema
                    click.echo("   📥 Input Schema:")
                    props = tool["input_schema"].get("properties", {})
                    required = tool["input_schema"].get("required", [])

                    if props:
                        for param_name, param_info in props.items():
                            required_mark = (
                                " (required)"
                                if param_name in required
                                else " (optional)"
                            )
                            param_type = param_info.get("type", "unknown")
                            param_desc = param_info.get("description", "No description")
                            default = param_info.get("default")
                            default_text = (
                                f" [default: {default}]" if default is not None else ""
                            )

                            click.echo(
                                f"     • {param_name} ({param_type}){required_mark}: {param_desc}{default_text}"
                            )
                    else:
                        click.echo("     No parameters required")
                    click.echo()

                    # Output Schema
                    if "output_schema" in tool:
                        click.echo("   📤 Output Schema:")
                        output_desc = tool["output_schema"].get(
                            "description", "No description"
                        )
                        click.echo(f"     {output_desc}")
                        output_props = tool["output_schema"].get("properties", {})
                        if output_props:
                            for prop_name, prop_info in output_props.items():
                                prop_desc = prop_info.get(
                                    "description", "No description"
                                )
                                click.echo(f"     • {prop_name}: {prop_desc}")
                        click.echo()

                    # Examples
                    if "examples" in tool:
                        click.echo("   💡 Usage Examples:")
                        for i, example in enumerate(tool["examples"], 1):
                            click.echo(f"     {i}. {example['description']}")
                            click.echo(f"        Input: {example['input']}")
                            click.echo(f"        Usage: {example['usage']}")
                            if i < len(tool["examples"]):
                                click.echo()
                        click.echo()

                click.echo("-" * 80)
                click.echo()
        else:  # text format
            click.echo("Available MCP Tools:")
            click.echo()

            for tool in tools_data:
                click.echo(f"• {tool['name']}: {tool['description']}")

                if verbose:
                    # Parameters
                    props = tool["input_schema"].get("properties", {})
                    required = tool["input_schema"].get("required", [])
                    if props:
                        click.echo("  Parameters:")
                        for param_name, param_info in props.items():
                            required_mark = (
                                " (required)"
                                if param_name in required
                                else " (optional)"
                            )
                            param_desc = param_info.get("description", "No description")
                            default = param_info.get("default")
                            default_text = (
                                f" [default: {default}]" if default is not None else ""
                            )
                            click.echo(
                                f"    - {param_name}{required_mark}: {param_desc}{default_text}"
                            )

                    # Examples
                    if "examples" in tool:
                        click.echo("  Examples:")
                        for example in tool["examples"]:
                            click.echo(
                                f"    - {example['description']}: {example['usage']}"
                            )
                            click.echo(f"      Input: {example['input']}")

                click.echo()

    anyio.run(run_tools)


def _get_server_instance(docs_path: pathlib.Path | None) -> TypstDocumentationServer:
    return TypstDocumentationServer(docs_path if docs_path else get_default_docs_path())


@tools.command("typst_search")
@click.argument("query", required=True)
@click.option(
    "--docs-path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=pathlib.Path
    ),
    help=f"Path to Typst documentation directory (default: {TYPST_VERSION} in project root)",
)
def search(query: str, docs_path: pathlib.Path | None) -> None:
    """Search through Typst documentation for specific topics, functions, or syntax.

    QUERY: The search term or phrase to find in the documentation.
    """

    async def run_search() -> None:
        server = _get_server_instance(docs_path)
        results = await server._handle_search(query)

        for result in results:
            click.echo(result.text)

    anyio.run(run_search)


@tools.command("typst_browse")
@click.option(
    "--depth",
    type=int,
    default=0,
    help="Maximum depth to traverse (0 for unlimited, default: 0)",
)
@click.option(
    "--sub-directory",
    "--dir",
    default=".",
    help="Subdirectory to explore (default: root)",
)
@click.option(
    "--docs-path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=pathlib.Path
    ),
    help=f"Path to Typst documentation directory (default: {TYPST_VERSION} in project root)",
)
def browse(depth: int, sub_directory: str, docs_path: pathlib.Path | None) -> None:
    """Browse the Typst documentation structure as a hierarchical tree."""

    async def run_browse() -> None:
        server = _get_server_instance(docs_path)
        results = await server._handle_browse(depth, sub_directory)

        for result in results:
            click.echo(result.text)

    anyio.run(run_browse)


@tools.command("typst_read")
@click.argument("path", required=True)
@click.option(
    "--docs-path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=pathlib.Path
    ),
    help=f"Path to Typst documentation directory (default: {TYPST_VERSION} in project root)",
)
def read(path: str, docs_path: pathlib.Path | None) -> None:
    """Read the content of a specific Typst documentation file.

    PATH: Relative path to the documentation file (e.g., 'reference/library/foundations/calc.md').
    """

    async def run_read() -> None:
        server = _get_server_instance(docs_path)
        results = await server._handle_read(path)

        for result in results:
            click.echo(result.text)

    anyio.run(run_read)


@cli.command()
@click.argument("pattern", required=True)
@click.option(
    "--docs-path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=pathlib.Path
    ),
    help=f"Path to Typst documentation directory (default: {TYPST_VERSION} in project root)",
)
def grep(pattern: str, docs_path: pathlib.Path | None) -> None:
    """Search for text patterns in documentation files."""
    server = _get_server_instance(docs_path)
    files = server._find_markdown_files()

    total_matches = 0

    for file_path in files:
        try:
            content = file_path.read_text(encoding="utf-8")
            lines = content.split("\n")

            matches = []
            for i, line in enumerate(lines):
                if pattern.lower() in line.lower():
                    matches.append((i + 1, line))

            if matches:
                relative_path = file_path.relative_to(server.docs_path)
                click.echo(f"📄 {relative_path}")
                for line_num, line in matches:
                    click.echo(f"Line {line_num}: {line}")
                click.echo()
                total_matches += len(matches)

        except Exception:
            continue

    click.echo(f"Total matches: {total_matches}")


# Add the tools group to the main CLI
cli.add_command(tools)


def main() -> None:
    """Entry point for the CLI application."""
    cli()


if __name__ == "__main__":
    main()
