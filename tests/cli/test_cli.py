"""Tests for CLI interface."""

from unittest.mock import patch, MagicMock
from pathlib import Path

# Import modules to test
from ai_architect_planner.cli.cli import process_project_details, main
from ai_architect_planner.utils.type_definitions import ProjectDetails

def test_process_project_details():
    """Test project creation process."""
    test_details = ProjectDetails(
        name="test-project",
        type="web",
        description="A test project"
    )
    
    mock_dir = Path("test-project")
    mock_doc_path = mock_dir / "docs" / "ARCHITECT.md"
    mock_content = "# Test Architecture"
    
    with patch('ai_architect_planner.cli.cli.create_project_structure') as mock_create, \
         patch('ai_architect_planner.cli.cli.save_architecture_doc') as mock_save, \
         patch('ai_architect_planner.cli.cli.generate_architecture_doc') as mock_generate, \
         patch('ai_architect_planner.cli.cli.show_success') as mock_show:
        
        # Set up mock returns
        mock_create.return_value = mock_dir
        mock_save.return_value = mock_doc_path
        mock_generate.return_value = mock_content
        
        process_project_details(test_details)
        
        mock_create.assert_called_once_with(test_details["name"])
        mock_generate.assert_called_once_with(test_details)
        mock_save.assert_called_once_with(mock_dir, mock_content)
        mock_show.assert_called_once_with(str(mock_dir), str(mock_doc_path))

def test_process_project_details_error():
    """Test error handling in project details processing."""
    test_details = ProjectDetails(
        name="test-project",
        type="web",
        description="A test project"
    )
    
    test_error = ValueError("Test error")
    
    with patch('ai_architect_planner.cli.cli.create_project_structure', side_effect=test_error), \
         patch('ai_architect_planner.cli.cli.show_error') as mock_show:
        
        try:
            process_project_details(test_details)
        except ValueError as e:
            assert str(e) == "Test error"
        
        mock_show.assert_called_once_with("Test error")

def test_main_success():
    """Test successful execution of main function."""
    test_details = ProjectDetails(
        name="test-project",
        type="web",
        description="A test project"
    )
    
    with patch('ai_architect_planner.cli.cli.collect_project_details') as mock_collect, \
         patch('ai_architect_planner.cli.cli.process_project_details') as mock_process:
        mock_collect.return_value = test_details
        mock_process.return_value = None
        
        result = main()
        
        mock_collect.assert_called_once()
        mock_process.assert_called_once_with(test_details)
        assert result == test_details

def test_main_keyboard_interrupt():
    """Test keyboard interrupt handling."""
    with patch('ai_architect_planner.cli.cli.collect_project_details', 
              side_effect=KeyboardInterrupt), \
         patch('ai_architect_planner.cli.cli.show_interrupt') as mock_show:
        result = main()
        assert result is None
        mock_show.assert_called_once()

def test_main_error():
    """Test general error handling."""
    with patch('ai_architect_planner.cli.cli.collect_project_details', 
              side_effect=Exception("Test error")), \
         patch('ai_architect_planner.cli.cli.show_error') as mock_show:
        result = main()
        assert result is None
        mock_show.assert_called_once_with("Test error")
