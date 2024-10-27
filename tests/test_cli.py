"""Tests for the interactive command-line interface."""

from unittest.mock import patch
from ai_architect_planner.cli import collect_project_details, process_project_details, main

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

def test_process_project_details():
    """Test project structure creation."""
    test_details = {
        "name": "test-project",
        "type": "web",
        "description": "A test project"
    }
    
    with patch('pathlib.Path.mkdir') as mock_mkdir, \
         patch('pathlib.Path.write_text') as mock_write:
        process_project_details(test_details)
        
        # Verify project structure creation
        assert mock_mkdir.call_count == 4  # project dir + src, docs, tests
        
        # Verify file content
        written_content = mock_write.call_args.args[0]
        assert "# test-project - Architecture Document" in written_content
        assert "**Project Name**: test-project" in written_content
        assert "**Project Type**: web" in written_content
        assert "**Description**: A test project" in written_content

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
    with patch('ai_architect_planner.cli.collect_project_details', side_effect=KeyboardInterrupt):
        result = main()
        assert result is None

def test_main_error():
    """Test general error handling."""
    with patch('ai_architect_planner.cli.collect_project_details', side_effect=Exception("Test error")):
        result = main()
        assert result is None
