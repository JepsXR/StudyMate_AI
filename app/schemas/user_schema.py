from pydantic import BaseModel, Field
from typing import List, Literal

# USERDATA DEVELOPING

class StudentData(BaseModel):

    name: str = Field(...,min_length=3, max_length=20)
    age: int = Field(...,gt=10, lt=100)
    strongest_learning_style: Literal["Visual", "Auditory", "Kinesthetic", "Reading/Writing", "Other"] = Field(...,)
    info_learning_style: str = Field(...,
        min_length=20, 
        max_length=100)
    available_hours_per_day: float = Field(gt=0, lt=24)
    study_subjects: List[str] = Field(
        default_factory=list, 
        max_length=4
        )
    concentration_level: Literal["Low", "Moderate", "High"] = Field(...,)
    info_exam: str = Field(
        ...,
        min_length=10,
        max_length=100)