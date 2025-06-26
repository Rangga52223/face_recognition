import numpy as np
import torch
def preprocess_face_for_embedding(face_img: np.ndarray) -> np.ndarray:
    """
    Input: RGB face image (112, 112, 3)
    Output: Normalized face image (1, 3, 112, 112) in float32 for ONNX
    """
    if face_img.shape != (112, 112, 3):
        raise ValueError(f"Expected (112,112,3), got {face_img.shape}")

    face_img = face_img.astype(np.float32) / 255.0
    face_img = (face_img - 0.5) / 0.5  # Normalize to [-1,1]
    face_img = np.transpose(face_img, (2, 0, 1))  # (3,112,112)
    face_img = np.expand_dims(face_img, axis=0)   # (1,3,112,112)
    return face_img