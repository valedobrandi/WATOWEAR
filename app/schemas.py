from pydantic import BaseModel, Field
from typing import List

# Input: What the user sends to the API
class OutfitRequest(BaseModel):
    clothes: List[str] = Field(..., min_length=1, description="List of available clothes in the wardrobe")
    occasion: str = Field(..., json_schema_extra={"example": "Business Meeting, Casual Outing, Formal Event, etc."})
    weather: str = Field(..., json_schema_extra={"example": "Cold and rainy"})
    style: str = Field(..., json_schema_extra={"example": "Minimalist, Bohemian, Classic, etc."})
    # New field: Default to 0.7 if not provided
    temperature: float = Field(0.7, ge=0, le=2.0, description="Creativity level of the AI")

# Output: What the API returns to the user
class OutfitResponse(BaseModel):
    outfit_name: str
    selected_items: List[str]
    style_advice: str