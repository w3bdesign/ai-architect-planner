"""Type definitions for AI Architect Planner."""

from typing import List, TypedDict, Literal

ProjectType = Literal["web", "mobile", "desktop", "api", "other"]

class ProjectDetails(TypedDict):
    """Project details type."""
    name: str
    type: ProjectType
    description: str

class ArchitectureAnalysis(TypedDict):
    """Architecture analysis type."""
    architecture: List[str]
    components: List[str]
    security: List[str]
    scalability: List[str]

class TechnologyStack(TypedDict):
    """Technology stack type."""
    frontend: List[str]
    backend: List[str]
    devops: List[str]
