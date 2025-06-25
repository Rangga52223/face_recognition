from app.db_model.database import SessionLocal
from app.db_model.face_save import FaceSave
from fastapi import HTTPException
import uuid

def save_face_embed(name, face_embed, image_base64):
    db = SessionLocal()
    try:
        cur = FaceSave(
            id_face=uuid.uuid4(),
            name=name,
            face_embed=face_embed,
            image_base64=image_base64
        ) 
        db.add(cur)
        db.commit()
        db.refresh(cur)
        db.close()
        return {"message": "Face registered successfully"}
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))