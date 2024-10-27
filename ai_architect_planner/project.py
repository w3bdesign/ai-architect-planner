"""Project structure and file operations."""

from pathlib import Path
from typing import Dict

def create_project_structure(project_name: str) -> Path:
    """Create the project directory structure."""
    project_dir = Path(project_name.lower().replace(" ", "-"))
    project_dir.mkdir(exist_ok=True)
    
    # Create standard subdirectories
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "docs").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    
    return project_dir

def save_architecture_doc(project_dir: Path, content: str) -> Path:
    """Save architecture document to the project docs directory."""
    output_path = project_dir / "docs" / "ARCHITECT.md"
    output_path.write_text(content, encoding='utf-8')
    return output_path
