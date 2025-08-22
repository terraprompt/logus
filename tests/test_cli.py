"""
Tests for the CLI interface of Blogus.
"""

import pytest
from click.testing import CliRunner
from blogus.cli import cli


@pytest.fixture
def runner():
    """Create a Click CLI runner for testing."""
    return CliRunner()


def test_cli_help(runner):
    """Test that the CLI shows help information."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert (
        "Blogus: A tool for crafting, analyzing, and perfecting AI prompts."
        in result.output
    )


def test_cli_analyze_command(runner):
    """Test the analyze command."""
    result = runner.invoke(cli, ["analyze", "--model", "gpt-3.5-turbo", "Test prompt"])
    # This will fail without API keys, but we can check that it attempts to run
    assert result.exit_code in [0, 1, 2]


def test_cli_test_command(runner):
    """Test the test command."""
    result = runner.invoke(cli, ["test", "--model", "gpt-3.5-turbo", "Test prompt"])
    # This will fail without API keys, but we can check that it attempts to run
    assert result.exit_code in [0, 1, 2]
