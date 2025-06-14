"""Tests for the CLI interface."""

import json
import pathlib
from unittest.mock import AsyncMock, Mock, patch

import pytest
from click.testing import CliRunner

from typst_mcp.cli import cli


class TestCLI:
    """Test the CLI interface."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a Click CLI runner for testing."""
        return CliRunner()

    def test_cli_help(self, runner: CliRunner) -> None:
        """Test the main CLI help command."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Typst MCP Server" in result.output
        assert "serve" in result.output
        assert "tools" in result.output
        assert "grep" in result.output

    def test_serve_help(self, runner: CliRunner) -> None:
        """Test the serve command help."""
        result = runner.invoke(cli, ["serve", "--help"])
        assert result.exit_code == 0
        assert "Start the MCP server" in result.output
        assert "--docs-path" in result.output
        assert "--debug" in result.output

    def test_tools_command_table_format(self, runner: CliRunner) -> None:
        """Test the tools list command with table format."""
        result = runner.invoke(cli, ["tools", "list"])
        assert result.exit_code == 0
        assert "Available MCP Tools" in result.output
        assert "typst_search" in result.output
        assert "typst_browse" in result.output
        assert "typst_read" in result.output
        assert "🔧" in result.output

    def test_tools_command_json_format(self, runner: CliRunner) -> None:
        """Test the tools list command with JSON format."""
        result = runner.invoke(cli, ["tools", "list", "--format", "json"])
        assert result.exit_code == 0

        # Parse the JSON output
        tools_data = json.loads(result.output)
        assert len(tools_data) == 3

        tool_names = [tool["name"] for tool in tools_data]
        assert "typst_search" in tool_names
        assert "typst_browse" in tool_names
        assert "typst_read" in tool_names

        # Check structure of first tool
        search_tool = next(t for t in tools_data if t["name"] == "typst_search")
        assert "description" in search_tool
        assert "input_schema" in search_tool
        assert "properties" in search_tool["input_schema"]
        assert "query" in search_tool["input_schema"]["properties"]
        # Check for enhanced features
        assert "output_schema" in search_tool
        assert "examples" in search_tool

    def test_tools_command_verbose(self, runner: CliRunner) -> None:
        """Test the tools list command with verbose flag."""
        result = runner.invoke(cli, ["tools", "list", "--verbose"])
        assert result.exit_code == 0
        assert "📥 Input Schema:" in result.output
        assert "📤 Output Schema:" in result.output
        assert "💡 Usage Examples:" in result.output
        assert "query (string) (required)" in result.output
        assert "depth (integer) (optional)" in result.output
        assert "path (string) (required)" in result.output

    def test_tools_command_text_format(self, runner: CliRunner) -> None:
        """Test the tools list command with text format."""
        result = runner.invoke(cli, ["tools", "list", "--format", "text"])
        assert result.exit_code == 0
        assert "Available MCP Tools:" in result.output
        assert "• typst_search:" in result.output
        assert "• typst_browse:" in result.output
        assert "• typst_read:" in result.output

    @patch("typst_mcp.cli.TypstDocumentationServer")
    def test_search_command(self, mock_server_class: Mock, runner: CliRunner) -> None:
        """Test the search command."""
        mock_server = Mock()
        mock_server_class.return_value = mock_server

        mock_result = Mock()
        mock_result.text = (
            "Search results for 'calc':\n\n📄 **calc.md**\nLine 1: calc function"
        )

        async def mock_search(query: str):
            return [mock_result]

        mock_server._handle_search = AsyncMock(side_effect=mock_search)

        result = runner.invoke(cli, ["tools", "typst_search", "calc"])
        assert result.exit_code == 0
        assert "Search results for 'calc'" in result.output
        assert "calc.md" in result.output
        mock_server._handle_search.assert_called_once_with("calc")

    @patch("typst_mcp.cli.TypstDocumentationServer")
    def test_browse_command(self, mock_server_class: Mock, runner: CliRunner) -> None:
        """Test the browse command."""
        mock_server = Mock()
        mock_server_class.return_value = mock_server

        mock_result = Mock()
        mock_result.text = "📁 Directory structure for: .\n\n📁 reference/\n📄 index.md"

        async def mock_browse(depth: int, sub_directory: str):
            return [mock_result]

        mock_server._handle_browse = AsyncMock(side_effect=mock_browse)

        result = runner.invoke(cli, ["tools", "typst_browse"])
        assert result.exit_code == 0
        assert "Directory structure" in result.output
        assert "📁 reference/" in result.output
        mock_server._handle_browse.assert_called_once_with(0, ".")

    @patch("typst_mcp.cli.TypstDocumentationServer")
    def test_browse_command_with_options(
        self, mock_server_class: Mock, runner: CliRunner
    ) -> None:
        """Test the browse command with depth and subdirectory options."""
        mock_server = Mock()
        mock_server_class.return_value = mock_server

        mock_result = Mock()
        mock_result.text = "📁 Directory structure for: reference\n\n📄 index.md"

        async def mock_browse(depth: int, sub_directory: str):
            return [mock_result]

        mock_server._handle_browse = AsyncMock(side_effect=mock_browse)

        result = runner.invoke(
            cli, ["tools", "typst_browse", "--depth", "2", "--dir", "reference"]
        )
        assert result.exit_code == 0
        mock_server._handle_browse.assert_called_once_with(2, "reference")

    @patch("typst_mcp.cli.TypstDocumentationServer")
    def test_read_command(self, mock_server_class: Mock, runner: CliRunner) -> None:
        """Test the read command."""
        mock_server = Mock()
        mock_server_class.return_value = mock_server

        mock_result = Mock()
        mock_result.text = "📄 **calc.md**\n\n# Calc Functions\n\nThe calc module..."

        async def mock_read(path: str):
            return [mock_result]

        mock_server._handle_read = AsyncMock(side_effect=mock_read)

        result = runner.invoke(
            cli, ["tools", "typst_read", "reference/library/foundations/calc.md"]
        )
        assert result.exit_code == 0
        assert "📄 **calc.md**" in result.output
        assert "# Calc Functions" in result.output
        mock_server._handle_read.assert_called_once_with(
            "reference/library/foundations/calc.md"
        )

    def test_list_files_command_not_implemented(self, runner: CliRunner) -> None:
        """Test that list-files command doesn't exist."""
        result = runner.invoke(cli, ["list-files"])
        assert result.exit_code != 0
        assert "No such command" in result.output

    def test_list_files_json_format_not_implemented(self, runner: CliRunner) -> None:
        """Test that list-files command with JSON format doesn't exist."""
        result = runner.invoke(cli, ["list-files", "--format", "json"])
        assert result.exit_code != 0
        assert "No such command" in result.output

    def test_info_command_not_implemented(self, runner: CliRunner) -> None:
        """Test that info command doesn't exist."""
        result = runner.invoke(cli, ["info"])
        assert result.exit_code != 0
        assert "No such command" in result.output

    @patch("typst_mcp.cli.TypstDocumentationServer")
    def test_grep_command(self, mock_server_class: Mock, runner: CliRunner) -> None:
        """Test the grep command."""
        mock_server = Mock()
        mock_server_class.return_value = mock_server

        mock_file = Mock(spec=pathlib.Path)
        mock_file.read_text.return_value = "Line 1\nThis contains calc function\nLine 3"
        mock_file.relative_to.return_value = pathlib.Path("calc.md")

        mock_server._find_markdown_files.return_value = [mock_file]
        mock_server.docs_path = pathlib.Path("/docs")

        result = runner.invoke(cli, ["grep", "calc"])
        assert result.exit_code == 0
        assert "📄 calc.md" in result.output
        assert "Line 2:" in result.output
        assert "This contains calc function" in result.output
        assert "Total matches: 1" in result.output

    def test_search_command_missing_query(self, runner: CliRunner) -> None:
        """Test search command without required query argument."""
        result = runner.invoke(cli, ["tools", "typst_search"])
        assert result.exit_code != 0
        assert "Missing argument" in result.output

    def test_read_command_missing_path(self, runner: CliRunner) -> None:
        """Test read command without required path argument."""
        result = runner.invoke(cli, ["tools", "typst_read"])
        assert result.exit_code != 0
        assert "Missing argument" in result.output

    def test_invalid_output_format(self, runner: CliRunner) -> None:
        """Test tools list command with invalid output format."""
        result = runner.invoke(cli, ["tools", "list", "--format", "invalid"])
        assert result.exit_code != 0
        assert "Invalid value for '--format'" in result.output

    @patch("anyio.run")
    def test_serve_command_basic(self, mock_anyio_run: Mock, runner: CliRunner) -> None:
        """Test the serve command basic functionality."""
        result = runner.invoke(cli, ["serve"])
        assert result.exit_code == 0
        assert "Starting Typst MCP Server..." in result.output
        assert "Server will communicate via stdio" in result.output
        assert "Using default documentation path: v0.13.1/" in result.output
        assert "Available tools:" in result.output
        mock_anyio_run.assert_called_once()

    @patch("anyio.run")
    def test_serve_command_with_debug(
        self, mock_anyio_run: Mock, runner: CliRunner
    ) -> None:
        """Test the serve command with debug flag."""
        result = runner.invoke(cli, ["serve", "--debug"])
        assert result.exit_code == 0
        assert "Debug mode enabled" in result.output
        mock_anyio_run.assert_called_once()

    def test_version_option(self, runner: CliRunner) -> None:
        """Test the version option."""
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        # The version output format may vary, just check it doesn't crash
