"""Integration tests for the Typst MCP Server."""

import pathlib
from unittest.mock import Mock, patch

import pytest

from typst_mcp.cli import get_default_docs_path
from typst_mcp.server import TypstDocumentationServer


class TestTypstMCPIntegration:
    """Integration tests for the complete MCP server functionality."""

    @pytest.fixture
    def server_instance(self) -> TypstDocumentationServer:
        """Create a server instance for integration testing."""
        with patch("pathlib.Path.exists", return_value=True):
            return TypstDocumentationServer(get_default_docs_path())

    def test_server_initialization(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test that server initializes correctly with all components."""
        assert server_instance.server.name == "typst-mcp"
        assert isinstance(server_instance.docs_path, pathlib.Path)
        assert server_instance.docs_path.name == "v0.13.1"

    @pytest.mark.anyio
    async def test_search_functionality_end_to_end(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test the complete search functionality from query to results."""
        # Create mock markdown files for testing
        mock_file1 = Mock(spec=pathlib.Path)
        mock_file1.read_text.return_value = (
            "# Functions\n\nThe `calc` function is used for calculations."
        )
        mock_file1.relative_to.return_value = pathlib.Path(
            "reference/library/foundations/calc.md"
        )

        mock_file2 = Mock(spec=pathlib.Path)
        mock_file2.read_text.return_value = (
            "# Math\n\nMath functions include calc operations."
        )
        mock_file2.relative_to.return_value = pathlib.Path(
            "reference/library/math/index.md"
        )

        with patch.object(
            server_instance,
            "_find_markdown_files",
            return_value=[mock_file1, mock_file2],
        ):
            result = await server_instance._handle_search("calc")

            assert len(result) == 1
            content = result[0].text
            assert "Search results for 'calc'" in content
            assert "reference/library/foundations/calc.md" in content
            assert "reference/library/math/index.md" in content

    @pytest.mark.anyio
    async def test_browse_functionality_end_to_end(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test the complete browse functionality."""
        # Mock directory structure
        mock_dir = Mock(spec=pathlib.Path)
        mock_dir.is_dir.return_value = True
        mock_dir.is_file.return_value = False
        mock_dir.name = "reference"

        mock_file = Mock(spec=pathlib.Path)
        mock_file.is_dir.return_value = False
        mock_file.is_file.return_value = True
        mock_file.name = "index.md"
        mock_file.suffix = ".md"

        mock_path = Mock(spec=pathlib.Path)
        mock_path.exists.return_value = True
        mock_path.iterdir.return_value = [mock_dir, mock_file]

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.__truediv__", return_value=mock_path),
        ):
            result = await server_instance._handle_browse(1, ".")

            assert len(result) == 1
            content = result[0].text
            assert "Directory structure for: ." in content
            assert "📁 reference/" in content
            assert "📄 index.md" in content

    @pytest.mark.anyio
    async def test_read_functionality_end_to_end(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test the complete read functionality."""
        test_content = """# Calc Function

The `calc` module provides mathematical functions and operations.

## Functions

- `calc.abs(x)`: Returns absolute value
- `calc.max(a, b)`: Returns maximum value
"""

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=True),
            patch("pathlib.Path.read_text", return_value=test_content),
        ):
            result = await server_instance._handle_read(
                "reference/library/foundations/calc.md"
            )

            assert len(result) == 1
            content = result[0].text
            assert "📄 **reference/library/foundations/calc.md**" in content
            assert "# Calc Function" in content
            assert "`calc.abs(x)`" in content

    @pytest.mark.anyio
    async def test_error_handling_across_all_tools(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test error handling across all tools."""
        # Test file not found for read
        with patch("pathlib.Path.exists", return_value=False):
            result = await server_instance._handle_read("nonexistent.md")
            assert "File not found" in result[0].text

        # Test directory not found for browse
        with patch("pathlib.Path.exists", return_value=False):
            result = await server_instance._handle_browse(0, "nonexistent")
            assert "Directory not found" in result[0].text

        # Test no results for search
        with patch.object(server_instance, "_find_markdown_files", return_value=[]):
            result = await server_instance._handle_search("nonexistent")
            assert "No results found" in result[0].text

    @pytest.mark.anyio
    async def test_large_search_results_pagination(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test that large search results are properly paginated."""
        # Create many mock files to test result limiting
        mock_files = []
        for i in range(15):  # More than the 10 file limit
            mock_file = Mock(spec=pathlib.Path)
            mock_file.read_text.return_value = f"Content {i} with search term"
            mock_file.relative_to.return_value = pathlib.Path(f"file_{i}.md")
            mock_files.append(mock_file)

        with patch.object(
            server_instance, "_find_markdown_files", return_value=mock_files
        ):
            result = await server_instance._handle_search("search")

            assert len(result) == 1
            content = result[0].text

            # Should only include first 10 files due to limiting
            assert "file_0.md" in content
            assert "file_9.md" in content
            assert "file_10.md" not in content  # Should be cut off

    @pytest.mark.anyio
    async def test_search_context_extraction(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test that search results include proper context around matches."""
        content_lines = [
            "Line 1: Introduction",
            "Line 2: Before context",
            "Line 3: This contains the search term we want",
            "Line 4: After context",
            "Line 5: Conclusion",
        ]

        mock_file = Mock(spec=pathlib.Path)
        mock_file.read_text.return_value = "\n".join(content_lines)
        mock_file.relative_to.return_value = pathlib.Path("test.md")

        with patch.object(
            server_instance, "_find_markdown_files", return_value=[mock_file]
        ):
            result = await server_instance._handle_search("search term")

            assert len(result) == 1
            content = result[0].text

            # Should include context lines around the match
            assert "Line 1: Introduction" in content  # 2 lines before
            assert "Line 2: Before context" in content  # 1 line before
            assert (
                "Line 3: This contains the search term we want" in content
            )  # Match line
            assert "Line 4: After context" in content  # 1 line after
            assert "Line 5: Conclusion" in content  # 2 lines after
            assert "Line 3" in content  # Line number should be shown

    def test_docs_path_resolution(self) -> None:
        """Test that the documentation path is correctly resolved."""
        with patch("pathlib.Path.exists", return_value=True):
            server = TypstDocumentationServer(get_default_docs_path())

        # Should use the default docs path
        assert server.docs_path == get_default_docs_path()
        assert server.docs_path.name == "v0.13.1"

    @pytest.mark.anyio
    async def test_file_encoding_handling(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test proper handling of file encoding."""
        content_with_unicode = "# Typst Functions\n\nMath symbols: ∑, ∫, π, λ"

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.is_file", return_value=True),
            patch("pathlib.Path.read_text", return_value=content_with_unicode),
        ):
            result = await server_instance._handle_read("unicode_test.md")

            assert len(result) == 1
            content = result[0].text
            assert "∑, ∫, π, λ" in content

    @pytest.mark.anyio
    async def test_empty_directory_browsing(
        self, server_instance: TypstDocumentationServer
    ) -> None:
        """Test browsing an empty directory."""
        mock_path = Mock(spec=pathlib.Path)
        mock_path.exists.return_value = True
        mock_path.iterdir.return_value = []

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.__truediv__", return_value=mock_path),
        ):
            result = await server_instance._handle_browse(0, "empty")

            assert len(result) == 1
            content = result[0].text
            assert "Directory structure for: empty" in content
