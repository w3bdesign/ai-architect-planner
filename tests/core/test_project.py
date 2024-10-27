"""Tests for project operations."""

from unittest.mock import patch
from pathlib import Path
from ai_architect_planner.core.project import create_project_structure, save_architecture_doc
from ai_architect_planner.utils.config import DEFAULT_DIRS

def test_create_project_structure():
    """Test project directory structure creation."""
    with patch('pathlib.Path.mkdir') as mock_mkdir:
        project_dir = create_project_structure("Test Project")
        assert str(project_dir) == "test-project"
        # Verify all directories are created
        assert mock_mkdir.call_count == len(DEFAULT_DIRS) + 1  # +1 for project dir

def test_save_architecture_doc():
    """Test saving architecture document."""
    test_content = "# Test Architecture"
    project_dir = Path("test-project")
    
    with patch('pathlib.Path.write_text') as mock_write:
        doc_path = save_architecture_doc(project_dir, test_content)
        assert doc_path == project_dir / "docs" / "ARCHITECT.md"
        mock_write.assert_called_once_with(test_content, encoding='utf-8')
