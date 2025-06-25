import numpy as np
from app.model.load_model import session
def get_embedding(face_array: np.ndarray) -> np.ndarray:
    """
    face_array: np.ndarray (shape: [112, 112, 3], RGB float32)
    return: embedding vector (512 dim)
    """
    # Ubah shape: (112,112,3) -> (1,3,112,112)
    face_input = np.transpose(face_array, (2, 0, 1))  # HWC -> CHW
    face_input = np.expand_dims(face_input, axis=0).astype(np.float32)

    embedding = session.run(None, {"input.1": face_input})[0]
    return embedding[0]