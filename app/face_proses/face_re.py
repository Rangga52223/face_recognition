from app.face_proses import *
from app.helper.save_embed import save_face_embed
from app.helper.load_embed import load_face_embed
from app.db_model.database import SessionLocal
from app.db_model.face_save import FaceSave

def register_face_re(name, content):
    try:
        nparr = np.frombuffer(content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_img = normalize_lighting(img)
        face_img = detect_and_align_face(face_img)
        face_base64 = encode_face_to_base64(face_img)
        if face_img is None:
            raise ValueError("No faces detected in image")
        preprocessed = preprocess_face_for_embedding(face_img)
        embedding = get_embedding(preprocessed)
        embedding = [float(x) for x in embedding]
        return save_face_embed(name, embedding, face_base64)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
def recognition_face_re(content):
    try:
        nparr = np.frombuffer(content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_img = normalize_lighting(img)
        face_img = detect_and_align_face(face_img)
        if face_img is None:
            raise ValueError("No faces detected in image")
        preprocessed = preprocess_face_for_embedding(face_img)
        embedding = get_embedding(preprocessed)
        embedding = [float(x) for x in embedding]
        face_embeds = load_face_embed()
        if not face_embeds:
            raise ValueError("No faces registered to recognize")
        match_results = match_face(embedding, face_embeds)
        if not match_results:
            raise ValueError("No face matches found")
        return match_results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

    
def delete_face_re(ids):
    try:
        face_id = ids
        db = SessionLocal()
        face = db.query(FaceSave).filter(FaceSave.id_face == face_id).first()
        if not face:
            return HTTPException(status_code=404, detail="Face not found")
        
        db.delete(face)
        db.commit()
        db.close()
        return {'message': f'Face with ID {face_id} has been deleted successfully'}

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

def get_all_face():
    try:
        face_list = load_face_embed()
        if face_list is None or len(face_list) == 0:
            return {"message": "Your data is empty"}

        result = []
        for face in face_list:  
            result.append({
                "id_face": str(face.id_face),
                "name": face.name,
                "image": face.image_base64  
            })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

