import numpy as np
def match_face(embedding_input, db_faces, threshold=0.6):
    best_score = -1
    best_match = None

    for face in db_faces:
        score = cosine_similarity(embedding_input, face.face_embed)
        if score > best_score:
            best_score = score
            best_match = face

    if best_score >= threshold:
        return {
            "match": True,
            "name": best_match.name,
            "id_face": str(best_match.id_face),
            "score": round(best_score, 4)
        }
    else:
        return {
            "match": False,
            "name": "unknown",
            "score": round(best_score, 4)
        }
    
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))