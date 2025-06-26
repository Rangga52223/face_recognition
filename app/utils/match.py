import numpy as np
def match_face(embedding_input, db_faces, threshold=0.62):
    print('DEBUG: match face')
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
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0  # bisa juga return -1.0 tergantung logika sistem kamu
    return np.dot(a, b) / denom
