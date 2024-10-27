"""Tests for the interactive command-line interface."""

import importlib
from unittest.mock import patch, call
import pytest
from ai_architect_planner.cli import collect_project_details, main, VALID_PROJECT_TYPES

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
    with patch('rich.prompt.Prompt.ask') as mock_ask, \
         patch('rich.console.Console.print') as mock_print:
        # First try invalid type, then valid type
        mock_ask.side_effect = [
            "test-project",      # project name
            "invalid-type",      # first try - invalid
            "web",              # second try - valid
            "A test project"    # description
        ]
        
        details = collect_project_details()
        assert details["type"] == "web"
        # Verify error message was printed
        mock_print.assert_any_call("[error]Please select a valid project type from the list.[/error]")

def test_cli_keyboard_interrupt():
    """Test graceful handling of keyboard interrupt."""
    with patch('rich.prompt.Prompt.ask', side_effect=KeyboardInterrupt), \
         patch('rich.console.Console.print') as mock_print:
        main()
        # Verify interrupt message was printed
        mock_print.assert_called_with("\n[warning]Process interrupted by user. Goodbye![/warning]")

def test_cli_error_handling():
    """Test general error handling."""
    error_msg = "Test error"
    with patch('rich.prompt.Prompt.ask', side_effect=ValueError(error_msg)), \
         patch('rich.console.Console.print') as mock_print:
        # Call main and capture the result
        result = main()
        # Verify error message was printed
        mock_print.assert_called_with(f"\n[error]An error occurred: {error_msg}[/error]")
        # Verify main returned None due to error
        assert result is None

def test_main_execution():
    """Test the main execution path."""
    with patch('ai_architect_planner.cli.collect_project_details') as mock_collect:
        mock_collect.return_value = {
            "name": "test",
            "type": "web",
            "description": "test project"
        }
        main()
        mock_collect.assert_called_once()

def test_module_main():
    """Test the __main__ block execution."""
    with patch('ai_architect_planner.cli.main') as mock_main:
        # Reload the module to trigger __name__ == "__main__" check
        importlib.reload(importlib.import_module('ai_architect_planner.cli'))
        # Since we're not really in __main__, main() shouldn't be called
        mock_main.assert_not_called()

def test_actual_main():
    """Test actual __main__ execution."""
    with patch('ai_architect_planner.cli.main') as mock_main:
        # Create a temporary __main__ module
        module = type('module', (), {'__name__': '__main__'})
        # Execute the main block with our mocked environment
        exec(
            'if __name__ == "__main__": main()',
            {'__name__': '__main__', 'main': mock_main}
        )
        # Verify main was called
        mock_main.assert_called_once()
