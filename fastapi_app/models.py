from sqlalchemy import Column, Integer, Float, String
from .database import Base

class ObjectDetectionResult(Base):
    __tablename__ = "object_detection_results"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    xmin_value = Column(Float, nullable=False)
    ymin = Column(Float, nullable=False)
    xmax_value = Column(Float, nullable=False)
    ymax = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    class_value = Column(Integer, nullable=False)  # 'class' is a reserved word in Python
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
