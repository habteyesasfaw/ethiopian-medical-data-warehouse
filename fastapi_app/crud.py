# # crud.py
# from sqlalchemy.orm import Session
# from models import ObjectDetection
# from schemas import ObjectDetectionCreate

# # Function to create a new object detection entry in the database
# def create_object_detection(db: Session, detection: ObjectDetectionCreate):
#     db_detection = ObjectDetection(**detection.dict())
#     db.add(db_detection)
#     db.commit()
#     db.refresh(db_detection)
#     return db_detection

# # Function to retrieve object detection by ID
# def get_detection_by_id(db: Session, detection_id: int):
#     return db.query(ObjectDetection).filter(ObjectDetection.id == detection_id).first()

# # Function to retrieve all object detections
# def get_detections(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(ObjectDetection).offset(skip).limit(limit).all()
from sqlalchemy.orm import Session
from . import models, schemas

def create_object_detection(db: Session, obj_data: schemas.ObjectDetectionCreate):
    db_object = models.ObjectDetectionResult(**obj_data.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def get_object_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ObjectDetectionResult).offset(skip).limit(limit).all()
