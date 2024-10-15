from pydantic import BaseModel

class ObjectDetectionBase(BaseModel):
    xmin_value: float
    ymin: float
    xmax_value: float
    ymax: float
    confidence: float
    class_value: int
    name: str
    image: str

class ObjectDetectionCreate(ObjectDetectionBase):
    pass

class ObjectDetection(ObjectDetectionBase):
    id: int

    class Config:
        orm_mode = True
