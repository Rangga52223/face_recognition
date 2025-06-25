# app/db_model/face_model.py

from sqlalchemy import Column, String, DateTime, Float, Text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from app.db_model.database import Base
import uuid
from datetime import datetime

class FaceSave(Base):
    __tablename__ = 'face_save'

    id_face = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String(255), nullable=True)
    face_embed = Column(ARRAY(Float), nullable=False)
    image_base64 = Column(Text, nullable=True)
