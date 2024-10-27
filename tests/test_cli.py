"""Tests for the interactive command-line interface."""

from unittest.mock import patch
from ai_architect_planner.cli import (
    collect_project_details,
    main,
    process_project_details,
    run_cli,
    VALID_PROJECT_TYPES
)

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
        result = main()
        # Verify interrupt message was printed
        mock_print.assert_called_with("\n[warning]Process interrupted by user. Goodbye![/warning]")
        assert result is None

def test_cli_error_handling():
    """Test general error handling."""
    error_msg = "Test error"
    with patch('rich.prompt.Prompt.ask', side_effect=ValueError(error_msg)), \
         patch('rich.console.Console.print') as mock_print:
        result = main()
        # Verify error message was printed
        mock_print.assert_called_with(f"\n[error]An error occurred: {error_msg}[/error]")
        assert result is None

def test_successful_main_execution():
    """Test successful execution path of main function."""
    test_details = {
        "name": "test-project",
        "type": "web",
        "description": "A test project"
    }
    
    with patch('ai_architect_planner.cli.collect_project_details') as mock_collect, \
         patch('ai_architect_planner.cli.process_project_details') as mock_process:
        # Set up the mock to return our test details
        mock_collect.return_value = test_details
        # Run main and ensure it completes without error
        result = main()
        # Verify collect_project_details was called
        mock_collect.assert_called_once()
        # Verify process_project_details was called with the correct arguments
        mock_process.assert_called_once_with(test_details)
        # Verify the result
        assert result == test_details

def test_process_project_details():
    """Test the process_project_details function."""
    test_details = {
        "name": "test-project",
        "type": "web",
        "description": "A test project"
    }
    # Should run without error
    process_project_details(test_details)

def test_run_cli():
    """Test the CLI entry point function."""
    with patch('ai_architect_planner.cli.main') as mock_main:
        run_cli()
        mock_main.assert_called_once()
