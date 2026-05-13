
from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class ProjectCategory(str, Enum):
    WEB_DEVELOPMENT = "Web Development"
    MOBILE_APP = "Mobile App"
    ARTIFICIAL_INTELLIGENCE = "AI"
    CYBER_SECURITY = "Cyber Security"

class IdeaSchema(BaseModel):
    """

    Schema for validating technology-based project ideas.
    """
    title: str = Field(..., min_length=3, max_length=50)
    detailed_description: str = Field(..., min_length=20, max_length=500)
    category: ProjectCategory
    required_tools: List[str] = Field(..., min_items=1)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Smart Irrigation",
                "detailed_description": "An automated system to water plants using sensors and Python.",
                "category": "AI",
                "required_tools": ["Python", "Raspberry Pi"]

            }
        }

def validate_idea_content(idea: IdeaSchema) -> bool:
    """
    Business logic function to perform additional custom validation.
    Checks if the title and description are not identical.
    """
    return idea.title.lower() != idea.detailed_description.lower()

def transform_idea_to_preview(idea: IdeaSchema) -> dict:
    """
    Logic function to transform raw data into a summary format.
    """
    return {

        "summary": f"{idea.title} - {idea.category}",
        "tools_count": len(idea.required_tools)
    }
#########################################################
#for try 
# if __name__=="__main__":
#     try:
#         test=IdeaSchema(
#             title="فكرة" ,
#             detailed_description="وصف قصير"  ,
#             category = "AI",
#             required_tools=["PC"])
#     except Exception as e:
#         print(" the code is right ")
#         print(e)
#########################################################