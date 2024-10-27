"""Tests for the command-line interface."""

from typer.testing import CliRunner
from ai_architect_planner.cli import app

runner = CliRunner()

def test_cli_requires_project_name():
    """Test that CLI requires project name."""
    result = runner.invoke(app)
    assert result.exit_code != 0
    assert "Missing option" in result.stdout

def test_cli_with_project_name():
    """Test CLI with project name."""
    result = runner.invoke(app, ["--project-name", "test-project"])
    assert result.exit_code == 0
    assert "Welcome to AI Architect Planner" in result.stdout
    assert "test-project" in result.stdout

def test_cli_custom_output_directory():
    """Test CLI with custom output directory."""
    result = runner.invoke(
        app,
        ["--project-name", "test-project", "--output-dir", "./custom-output"]
    )
    assert result.exit_code == 0
    assert "custom-output" in result.stdout
