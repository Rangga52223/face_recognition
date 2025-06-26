import numpy as np
import torch
def preprocess_face_for_embedding(face_img: np.ndarray) -> np.ndarray:
    print("Shape masuk preprocess_face_for_embedding:", face_img.shape)
    if isinstance(face_img, torch.Tensor):
        face_img = face_img.permute(1, 2, 0).cpu().numpy()

    if face_img.ndim != 3 or face_img.shape[2] != 3:
        raise ValueError(f"Expected image shape (H,W,3), got {face_img.shape}")

    face_img = face_img.astype(np.float32) / 255.0
    face_img = (face_img - 0.5) / 0.5

    print("Shape sebelum transpose:", face_img.shape)  # Tambahkan ini

    if face_img.shape != (112, 112, 3):
        raise ValueError(f"Shape before transpose must be (112,112,3), got {face_img.shape}")

    face_img = np.transpose(face_img, (2, 0, 1))  # [3,112,112]
    face_img = np.expand_dims(face_img, axis=0)   # [1,3,112,112]
    return face_img