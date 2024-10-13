# schemas.py
from pydantic import BaseModel

# Pydantic schema for the Object Detection result
class ObjectDetectionBase(BaseModel):
    image_url: str
    object_class: str
    confidence_score: float
    bounding_box: str  # Could also be a list of coordinates

    class Config:
        orm_mode = True

# Schema for creating object detection result
class ObjectDetectionCreate(ObjectDetectionBase):
    pass

# Schema for reading object detection result
class ObjectDetection(ObjectDetectionBase):
    id: int
