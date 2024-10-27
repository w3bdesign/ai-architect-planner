"""Tests for user interaction."""

from unittest.mock import patch
from ai_architect_planner.core.interaction import (
    collect_project_details,
    show_success,
    show_error,
    show_interrupt
)
from ai_architect_planner.utils.constants import (
    INVALID_TYPE_ERROR,
    ERROR_MESSAGE,
    INTERRUPT_MESSAGE,
    SUCCESS_CREATE,
    SUCCESS_SAVE
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
    with patch('rich.prompt.Prompt.ask') as mock_ask, \
         patch('rich.console.Console.print') as mock_print:
        mock_ask.side_effect = [
            "test-project",
            "invalid",
            "web",
            "A test project"
        ]
        
        details = collect_project_details()
        assert details["type"] == "web"
        mock_print.assert_any_call(INVALID_TYPE_ERROR)

def test_show_messages():
    """Test showing various messages."""
    project_dir = "test-project"
    doc_path = "test-project/docs/ARCHITECT.md"
    error_msg = "Test error"
    
    with patch('rich.console.Console.print') as mock_print:
        show_success(project_dir, doc_path)
        show_error(error_msg)
        show_interrupt()
        
        mock_print.assert_any_call(SUCCESS_CREATE.format(project_dir))
        mock_print.assert_any_call(SUCCESS_SAVE.format(doc_path))
        mock_print.assert_any_call(ERROR_MESSAGE.format(error_msg))
        mock_print.assert_any_call(INTERRUPT_MESSAGE)
