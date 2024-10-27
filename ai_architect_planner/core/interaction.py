"""User interaction and prompts."""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from ai_architect_planner.utils.type_definitions import ProjectDetails
from ai_architect_planner.utils.config import PROJECT_TYPES
from ai_architect_planner.utils.constants import (
    WELCOME_MESSAGE,
    PROJECT_NAME_PROMPT,
    PROJECT_TYPE_PROMPT,
    PROJECT_DESC_PROMPT,
    INVALID_TYPE_ERROR,
    INTERRUPT_MESSAGE,
    ERROR_MESSAGE,
    SUCCESS_CREATE,
    SUCCESS_SAVE,
)

console = Console()

def collect_project_details() -> ProjectDetails:
    """Collect project details through interactive prompts."""
    console.print(
        Panel.fit(
            WELCOME_MESSAGE,
            title="AI Architect Planner",
        )
    )

    project_name = Prompt.ask(PROJECT_NAME_PROMPT)
    
    while True:
        project_type = Prompt.ask(
            PROJECT_TYPE_PROMPT,
            choices=PROJECT_TYPES,
            show_choices=True
        )
        if project_type in PROJECT_TYPES:
            break
        console.print(INVALID_TYPE_ERROR)
    
    project_description = Prompt.ask(PROJECT_DESC_PROMPT)
    
    return {
        "name": project_name,
        "type": project_type,
        "description": project_description
    }

def show_success(project_dir: str, doc_path: str) -> None:
    """Show success messages."""
    console.print(SUCCESS_CREATE.format(project_dir))
    console.print(SUCCESS_SAVE.format(doc_path))

def show_error(message: str) -> None:
    """Show error message."""
    console.print(ERROR_MESSAGE.format(message))

def show_interrupt() -> None:
    """Show interrupt message."""
    console.print(INTERRUPT_MESSAGE)
