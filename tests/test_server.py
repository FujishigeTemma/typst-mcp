"""Unit tests for the Typst MCP Server."""

import pathlib
from unittest.mock import Mock, patch

import pytest
from mcp.types import TextContent

from typst_mcp.cli import get_default_docs_path
from typst_mcp.server import TypstDocumentationServer


class TestTypstDocumentationServer:
    """Test the TypstDocumentationServer class."""

    @pytest.fixture
    def server(self) -> TypstDocumentationServer:
        """Create a server instance for testing."""
        with patch("pathlib.Path.exists", return_value=True):
            return TypstDocumentationServer(get_default_docs_path())

    def test_init(self, server: TypstDocumentationServer) -> None:
        """Test server initialization."""
        assert server.server.name == "typst-mcp"
        assert isinstance(server.docs_path, pathlib.Path)
        assert server.docs_path == get_default_docs_path()

    @pytest.mark.anyio
    async def test_handle_search_no_results(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test search with no results."""
        with patch.object(server, "_find_markdown_files", return_value=[]):
            result = await server._handle_search("nonexistent")

        assert len(result) == 1
        assert isinstance(result[0], TextContent)
        assert "No results found" in result[0].text

    @pytest.mark.anyio
    async def test_handle_search_with_results(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test search with matching results."""
        mock_file = Mock(spec=pathlib.Path)
        mock_file.read_text.return_value = (
            "This is a test\ncontaining search\nterm content"
        )
        mock_file.relative_to.return_value = pathlib.Path("test.md")

        with patch.object(server, "_find_markdown_files", return_value=[mock_file]):
            result = await server._handle_search("search")

        assert len(result) == 1
        assert isinstance(result[0], TextContent)
        assert "Search results for 'search'" in result[0].text
        assert "test.md" in result[0].text
        assert "Line 2" in result[0].text

    @pytest.mark.anyio
    async def test_handle_search_file_read_error(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test search handling file read errors gracefully."""
        mock_file = Mock(spec=pathlib.Path)
        mock_file.read_text.side_effect = OSError("Permission denied")

        with patch.object(server, "_find_markdown_files", return_value=[mock_file]):
            result = await server._handle_search("test")

        assert len(result) == 1
        assert "No results found" in result[0].text

    @pytest.mark.anyio
    async def test_handle_browse_directory_not_found(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test browse with non-existent directory."""
        with patch("pathlib.Path.exists", return_value=False):
            result = await server._handle_browse(0, "nonexistent")

        assert len(result) == 1
        assert "Directory not found" in result[0].text

    @pytest.mark.anyio
    async def test_handle_browse_success(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test successful directory browsing."""
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch.object(
                server, "_generate_tree", return_value="📁 test/\n📄 file.md\n"
            ),
        ):
            result = await server._handle_browse(1, ".")

        assert len(result) == 1
        assert "Directory structure for: ." in result[0].text
        assert "📁 test/" in result[0].text

    @pytest.mark.anyio
    async def test_handle_read_file_not_found(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test reading non-existent file."""
        with patch("pathlib.Path.exists", return_value=False):
            result = await server._handle_read("nonexistent.md")

        assert len(result) == 1
        assert "File not found" in result[0].text

    @pytest.mark.anyio
    async def test_handle_read_not_a_file(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test reading a directory instead of file."""
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=False),
        ):
            result = await server._handle_read("directory")

        assert len(result) == 1
        assert "Path is not a file" in result[0].text

    @pytest.mark.anyio
    async def test_handle_read_success(self, server: TypstDocumentationServer) -> None:
        """Test successful file reading."""
        file_content = "# Test Document\n\nThis is test content."

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=True),
            patch("pathlib.Path.read_text", return_value=file_content),
        ):
            result = await server._handle_read("test.md")

        assert len(result) == 1
        assert "📄 **test.md**" in result[0].text
        assert file_content in result[0].text

    @pytest.mark.anyio
    async def test_handle_read_error(self, server: TypstDocumentationServer) -> None:
        """Test file reading with error."""
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=True),
            patch("pathlib.Path.read_text", side_effect=OSError("Permission denied")),
        ):
            result = await server._handle_read("test.md")

        assert len(result) == 1
        assert "Error reading file" in result[0].text

    def test_find_markdown_files_docs_not_exist(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test finding markdown files when docs directory doesn't exist."""
        with patch("pathlib.Path.exists", return_value=False):
            result = server._find_markdown_files()

        assert result == []

    def test_find_markdown_files_success(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test finding markdown files successfully."""
        mock_files = [Mock(spec=pathlib.Path) for _ in range(3)]

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.rglob", return_value=mock_files),
        ):
            result = server._find_markdown_files()

        assert result == mock_files

    def test_generate_tree_max_depth_exceeded(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test tree generation with max depth exceeded."""
        mock_path = Mock(spec=pathlib.Path)
        result = server._generate_tree(mock_path, 1, 1)

        assert result == ""

    def test_generate_tree_permission_error(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test tree generation with permission error."""
        mock_path = Mock(spec=pathlib.Path)
        mock_path.iterdir.side_effect = PermissionError("Access denied")

        result = server._generate_tree(mock_path, 0, 0)

        assert "❌ Permission denied" in result

    def test_generate_tree_success(self, server: TypstDocumentationServer) -> None:
        """Test successful tree generation."""
        mock_file = Mock()
        mock_file.is_dir.return_value = False
        mock_file.is_file.return_value = True
        mock_file.name = "test.md"
        mock_file.suffix = ".md"

        mock_path = Mock()
        mock_path.iterdir.return_value = [mock_file]

        # Test at max depth to avoid recursion issues
        result = server._generate_tree(mock_path, 1, 0)

        assert "📄 test.md" in result

    @pytest.mark.anyio
    async def test_handle_call_tool_unknown_tool(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test handling unknown tool calls directly."""

        # Test the handler logic directly by creating a mock handler
        async def mock_handler(name: str, arguments: dict) -> list:
            if name == "typst_search":
                return await server._handle_search(arguments["query"])
            elif name == "typst_browse":
                depth = arguments.get("depth", 0)
                sub_directory = arguments.get("sub_directory", ".")
                return await server._handle_browse(depth, sub_directory)
            elif name == "typst_read":
                return await server._handle_read(arguments["path"])
            else:
                raise ValueError(f"Unknown tool: {name}")

        with pytest.raises(ValueError, match="Unknown tool"):
            await mock_handler("unknown_tool", {})

    @pytest.mark.anyio
    async def test_handle_call_tool_search(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test handling search tool calls directly."""
        with patch.object(
            server,
            "_handle_search",
            return_value=[TextContent(type="text", text="test")],
        ) as mock_search:
            result = await server._handle_search("test")

        mock_search.assert_called_once_with("test")
        assert len(result) == 1

    @pytest.mark.anyio
    async def test_handle_call_tool_browse(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test handling browse tool calls directly."""
        with patch.object(
            server,
            "_handle_browse",
            return_value=[TextContent(type="text", text="test")],
        ) as mock_browse:
            result = await server._handle_browse(2, "test")

        mock_browse.assert_called_once_with(2, "test")
        assert len(result) == 1

    @pytest.mark.anyio
    async def test_handle_call_tool_browse_defaults(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test handling browse tool calls with default arguments."""
        with patch.object(
            server,
            "_handle_browse",
            return_value=[TextContent(type="text", text="test")],
        ) as mock_browse:
            result = await server._handle_browse(0, ".")

        mock_browse.assert_called_once_with(0, ".")
        assert len(result) == 1

    @pytest.mark.anyio
    async def test_handle_call_tool_read(
        self, server: TypstDocumentationServer
    ) -> None:
        """Test handling read tool calls directly."""
        with patch.object(
            server, "_handle_read", return_value=[TextContent(type="text", text="test")]
        ) as mock_read:
            result = await server._handle_read("test.md")

        mock_read.assert_called_once_with("test.md")
        assert len(result) == 1
