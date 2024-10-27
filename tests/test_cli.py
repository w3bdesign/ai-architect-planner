"""Tests for CLI interface."""

from unittest.mock import patch
from ai_architect_planner.cli import process_project_details, main

def test_process_project_details():
    """Test project creation process."""
    test_details = {
        "name": "test-project",
        "type": "web",
        "description": "A test project"
    }
    
    with patch('ai_architect_planner.cli.create_project_structure') as mock_create, \
         patch('ai_architect_planner.cli.save_architecture_doc') as mock_save, \
         patch('ai_architect_planner.cli.generate_architecture_doc') as mock_generate, \
         patch('ai_architect_planner.cli.show_success') as mock_show:
        
        # Set up mock returns
        mock_create.return_value = "test-project"
        mock_save.return_value = "test-project/docs/ARCHITECT.md"
        mock_generate.return_value = "# Test Architecture"
        
        process_project_details(test_details)
        
        mock_create.assert_called_once_with(test_details["name"])
        mock_generate.assert_called_once_with(test_details)
        mock_save.assert_called_once()
        mock_show.assert_called_once()

def test_main_success():
    """Test successful execution of main function."""
    test_details = {
        "name": "test-project",
        "type": "web",
        "description": "A test project"
    }
    
    with patch('ai_architect_planner.cli.collect_project_details') as mock_collect, \
         patch('ai_architect_planner.cli.process_project_details') as mock_process:
        mock_collect.return_value = test_details
        result = main()
        
        mock_collect.assert_called_once()
        mock_process.assert_called_once_with(test_details)
        assert result == test_details

def test_main_keyboard_interrupt():
    """Test keyboard interrupt handling."""
    with patch('ai_architect_planner.cli.collect_project_details', 
              side_effect=KeyboardInterrupt), \
         patch('ai_architect_planner.cli.show_interrupt') as mock_show:
        result = main()
        assert result is None
        mock_show.assert_called_once()

def test_main_error():
    """Test general error handling."""
    with patch('ai_architect_planner.cli.collect_project_details', 
              side_effect=Exception("Test error")), \
         patch('ai_architect_planner.cli.show_error') as mock_show:
        result = main()
        assert result is None
        mock_show.assert_called_once_with("Test error")
