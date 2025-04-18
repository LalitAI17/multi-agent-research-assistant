"""
Schema definitions for the analysts module.
"""

from typing import List
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

class Analyst(BaseModel):
    """Schema for an analyst."""
    
    affiliation: str = Field(
        description="Primary affiliation of the analyst.",
    )
    name: str = Field(
        description="Name of the analyst."
    )
    role: str = Field(
        description="Role of the analyst in the context of the topic.",
    )
    description: str = Field(
        description="Description of the analyst focus, concerns, and motives.",
    )
    
    @property
    def persona(self) -> str:
        """Format the analyst information as a persona description."""
        return f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affiliation}\nDescription: {self.description}\n"

class Perspectives(BaseModel):
    """Collection of analysts for a research topic."""
    
    analysts: List[Analyst] = Field(
        description="Comprehensive list of analysts with their roles and affiliations.",
    ) 


class GenerateAnalystsState(TypedDict):
    """State for the analyst generation graph."""
    topic: str  # Research topic
    max_analysts: int  # Number of analysts
    human_analyst_feedback: str  # Human feedback
    analysts: List[Analyst]  # Generated analysts 