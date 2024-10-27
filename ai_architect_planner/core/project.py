"""Project structure and file operations."""

from pathlib import Path
from ai_architect_planner.utils.config import DEFAULT_DIRS, get_doc_path

def create_project_structure(project_name: str) -> Path:
    """Create the project directory structure."""
    project_dir = Path(project_name.lower().replace(" ", "-"))
    project_dir.mkdir(exist_ok=True)
    
    # Create standard subdirectories
    for dir_name in DEFAULT_DIRS:
        (project_dir / dir_name).mkdir(exist_ok=True)
    
    return project_dir

def save_architecture_doc(project_dir: Path, content: str) -> Path:
    """Save architecture document to the project docs directory."""
    output_path = get_doc_path(project_dir)
    output_path.write_text(content, encoding='utf-8')
    return output_path
