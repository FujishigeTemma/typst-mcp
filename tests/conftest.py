"""Shared test fixtures and configuration for pytest."""

import pathlib
import tempfile
from typing import Iterator
from unittest.mock import Mock, patch

import pytest

from typst_mcp.server import TypstDocumentationServer


@pytest.fixture
def temp_docs_dir() -> Iterator[pathlib.Path]:
    """Create a temporary directory structure for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        docs_path = pathlib.Path(temp_dir)

        # Create sample directory structure
        (docs_path / "reference").mkdir()
        (docs_path / "reference" / "library").mkdir()
        (docs_path / "reference" / "library" / "foundations").mkdir()
        (docs_path / "guides").mkdir()

        # Create sample markdown files
        (docs_path / "index.md").write_text("# Typst Documentation")
        (docs_path / "reference" / "index.md").write_text("# Reference")
        (docs_path / "reference" / "library" / "index.md").write_text("# Library")
        (docs_path / "reference" / "library" / "foundations" / "calc.md").write_text(
            "# Calc Functions\n\nThe calc module provides mathematical functions."
        )
        (docs_path / "guides" / "getting-started.md").write_text(
            "# Getting Started\n\nThis guide helps you get started with Typst."
        )

        yield docs_path


@pytest.fixture
def mock_server() -> TypstDocumentationServer:
    """Create a mock server instance for testing."""
    with patch("pathlib.Path.exists", return_value=True):
        server = TypstDocumentationServer(pathlib.Path("/mock/docs"))
        return server


@pytest.fixture
def sample_markdown_files() -> list[Mock]:
    """Create sample markdown file mocks for testing."""
    files = []

    # File 1: calc.md
    calc_file = Mock(spec=pathlib.Path)
    calc_file.read_text.return_value = """# Calc Functions

The `calc` module provides mathematical functions and operations.

## Functions

- `calc.abs(x)`: Returns the absolute value of x
- `calc.max(a, b)`: Returns the maximum of a and b
- `calc.min(a, b)`: Returns the minimum of a and b
"""
    calc_file.relative_to.return_value = pathlib.Path(
        "reference/library/foundations/calc.md"
    )
    files.append(calc_file)

    # File 2: string.md
    string_file = Mock(spec=pathlib.Path)
    string_file.read_text.return_value = """# String Functions

String manipulation functions in Typst.

## Methods

- `str.len()`: Returns string length
- `str.contains(pattern)`: Check if string contains pattern
"""
    string_file.relative_to.return_value = pathlib.Path(
        "reference/library/foundations/str.md"
    )
    files.append(string_file)

    # File 3: guide.md
    guide_file = Mock(spec=pathlib.Path)
    guide_file.read_text.return_value = """# Getting Started Guide

Welcome to Typst! This guide will help you get started.

## Installation

Download and install Typst from the official website.
"""
    guide_file.relative_to.return_value = pathlib.Path("guides/getting-started.md")
    files.append(guide_file)

    return files


@pytest.fixture
def sample_directory_structure() -> Mock:
    """Create a sample directory structure mock for testing."""
    # Create mock directory and file objects
    root_dir = Mock(spec=pathlib.Path)
    root_dir.exists.return_value = True

    # Reference directory
    ref_dir = Mock(spec=pathlib.Path)
    ref_dir.is_dir.return_value = True
    ref_dir.is_file.return_value = False
    ref_dir.name = "reference"

    # Library directory
    lib_dir = Mock(spec=pathlib.Path)
    lib_dir.is_dir.return_value = True
    lib_dir.is_file.return_value = False
    lib_dir.name = "library"

    # Foundations directory
    foundations_dir = Mock(spec=pathlib.Path)
    foundations_dir.is_dir.return_value = True
    foundations_dir.is_file.return_value = False
    foundations_dir.name = "foundations"

    # Sample files
    index_file = Mock(spec=pathlib.Path)
    index_file.is_dir.return_value = False
    index_file.is_file.return_value = True
    index_file.name = "index.md"
    index_file.suffix = ".md"

    calc_file = Mock(spec=pathlib.Path)
    calc_file.is_dir.return_value = False
    calc_file.is_file.return_value = True
    calc_file.name = "calc.md"
    calc_file.suffix = ".md"

    # Set up directory structure
    root_dir.iterdir.return_value = [ref_dir, index_file]
    ref_dir.iterdir.return_value = [lib_dir]
    lib_dir.iterdir.return_value = [foundations_dir]
    foundations_dir.iterdir.return_value = [calc_file]

    return root_dir


@pytest.fixture(autouse=True)
def anyio_backend() -> str:
    """Configure anyio backend for async tests."""
    return "asyncio"


@pytest.fixture
def search_results_sample() -> dict[str, str]:
    """Sample search results for testing."""
    return {
        "calc": "Mathematical calculations and functions",
        "string": "Text manipulation and string operations",
        "guide": "Documentation and tutorials",
        "typst": "The Typst markup language",
    }


@pytest.fixture
def mock_file_content() -> dict[str, str]:
    """Mock file contents for different file types."""
    return {
        "calc.md": """# Mathematical Functions

The calc module provides mathematical operations.

## Basic Functions
- abs(x): Absolute value
- max(a, b): Maximum value
- min(a, b): Minimum value

## Advanced Functions
- sin(x): Sine function
- cos(x): Cosine function
""",
        "string.md": """# String Operations

String manipulation in Typst.

## Methods
- len(): Get string length
- contains(pattern): Check if contains pattern
- replace(old, new): Replace text
""",
        "index.md": """# Typst Documentation

Welcome to the Typst documentation.

## Sections
- Reference: Complete API reference
- Guides: Step-by-step tutorials
- Examples: Code samples
""",
    }


@pytest.fixture
def error_scenarios() -> dict[str, Exception]:
    """Common error scenarios for testing."""
    return {
        "permission_denied": PermissionError("Permission denied"),
        "file_not_found": FileNotFoundError("File not found"),
        "io_error": OSError("I/O operation failed"),
        "encoding_error": UnicodeDecodeError("utf-8", b"", 0, 1, "invalid start byte"),
    }
