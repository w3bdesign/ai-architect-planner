"""Tests for the interactive command-line interface."""

from unittest.mock import patch
from typer.testing import CliRunner
from ai_architect_planner.cli import app, collect_project_details, VALID_PROJECT_TYPES

runner = CliRunner()

def test_cli_starts():
    """Test that CLI starts successfully."""
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        # Simulate user inputs
        mock_ask.side_effect = [
            "test-project",  # project name
            "web",          # project type
            "A test project" # description
        ]
        
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "Welcome to AI Architect Planner" in result.stdout

def test_project_details_collection():
    """Test project details collection through interactive prompts."""
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        # Simulate user inputs
        mock_ask.side_effect = [
            "test-project",
            "api",
            "A test API project"
        ]
        
        details = collect_project_details()
        
        assert details["name"] == "test-project"
        assert details["type"] == "api"
        assert details["description"] == "A test API project"

def test_project_type_validation():
    """Test that project type must be one of the valid choices."""
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        mock_ask.side_effect = [
            "test-project",  # project name
            "web",          # valid project type
            "A test project" # description
        ]
        
        details = collect_project_details()
        assert details["type"] in VALID_PROJECT_TYPES
        assert details["type"] == "web"

def test_cli_keyboard_interrupt():
    """Test graceful handling of keyboard interrupt."""
    with patch('rich.prompt.Prompt.ask', side_effect=KeyboardInterrupt):
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "interrupted by user" in result.stdout.lower()

def test_cli_error_handling():
    """Test general error handling."""
    with patch('rich.prompt.Prompt.ask', side_effect=Exception("Test error")):
        result = runner.invoke(app)
        assert result.exit_code == 0
        assert "an error occurred" in result.stdout.lower()
        assert "test error" in result.stdout.lower()
