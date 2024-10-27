"""Interactive console interface for AI Architect Planner."""

from typing import Optional
from pathlib import Path

# Import from core modules
from ai_architect_planner.core.interaction import (
    collect_project_details,
    show_success,
    show_error,
    show_interrupt
)
from ai_architect_planner.core.project import (
    create_project_structure,
    save_architecture_doc
)

# Import from services
from ai_architect_planner.services.llm import generate_architecture_doc

# Import from utils
from ai_architect_planner.utils.type_definitions import ProjectDetails

def process_project_details(details: ProjectDetails) -> None:
    """Process the collected project details and create project structure."""
    try:
        # Create project structure
        project_dir = create_project_structure(details["name"])
        
        # Generate and save architecture document
        content = generate_architecture_doc(details)
        doc_path = save_architecture_doc(project_dir, content)
        
        # Show success messages
        show_success(str(project_dir), str(doc_path))
    except Exception as e:
        show_error(str(e))
        raise

def main() -> Optional[ProjectDetails]:
    """Start the interactive AI Architect planning process."""
    try:
        details = collect_project_details()
        process_project_details(details)
        return details
    except KeyboardInterrupt:
        show_interrupt()
        return None
    except Exception as e:
        show_error(str(e))
        return None
