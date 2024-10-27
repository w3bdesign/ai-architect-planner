"""Tests for user interaction."""

from unittest.mock import patch
from ai_architect_planner.interaction import (
    collect_project_details,
    show_success,
    show_error,
    show_interrupt
)

def test_collect_project_details():
    """Test project details collection through interactive prompts."""
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        mock_ask.side_effect = [
            "test-project",
            "web",
            "A test project"
        ]
        
        details = collect_project_details()
        assert details == {
            "name": "test-project",
            "type": "web",
            "description": "A test project"
        }

def test_invalid_project_type():
    """Test handling of invalid project type."""
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        mock_ask.side_effect = [
            "test-project",
            "invalid",
            "web",
            "A test project"
        ]
        
        details = collect_project_details()
        assert details["type"] == "web"

def test_show_messages():
    """Test showing various messages."""
    with patch('rich.console.Console.print') as mock_print:
        show_success("test-project", "test-project/docs/ARCHITECT.md")
        show_error("Test error")
        show_interrupt()
        
        assert mock_print.call_count == 4  # 2 success messages + error + interrupt
