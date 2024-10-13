from sqlalchemy import Column, Integer, String, Float
from database import Base

# SQLAlchemy model representing the object detection table
class ObjectDetection(Base):
    __tablename__ = "object_detection_results"
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, index=True)
    object_class = Column(String)
    confidence_score = Column(Float)
    bounding_box = Column(String)  # Store as JSON or a string representing coordinates
