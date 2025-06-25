from app.db_model.database import SessionLocal
from app.db_model.face_save import FaceSave

def load_face_embed():
    db = SessionLocal()
    try:
        face_embeds = db.query(FaceSave).all()
        db.close()
        return face_embeds
    except Exception as e:
        db.close()
        raise Exception(f"Error loading face embeddings: {str(e)}") from e