"""Configuration settings for AI Architect Planner."""

from pathlib import Path

# Project structure
DEFAULT_DIRS = ["src", "docs", "tests"]
ARCHITECT_DOC_NAME = "ARCHITECT.md"

# Valid project types
PROJECT_TYPES = ["web", "mobile", "desktop", "api", "other"]

# File paths
def get_doc_path(project_dir: Path) -> Path:
    """Get the path for the architecture document."""
    return project_dir / "docs" / ARCHITECT_DOC_NAME
