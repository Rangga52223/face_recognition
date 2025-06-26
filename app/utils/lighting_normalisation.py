import cv2
import numpy as np

def normalize_lighting(image: np.ndarray) -> np.ndarray:
    """
    Normalisasi pencahayaan dengan CLAHE pada channel L gambar RGB
    """
    print("Shape after detect_and_align_face:", image.shape)
    print('DEBUG: lighting')
    
    if image is None:
        raise ValueError("Input gambar kosong")

    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError(f"Gambar harus RGB (H, W, 3), dapat shape: {image.shape}")

    if image.dtype != np.uint8:
        image = (image * 255).astype(np.uint8)  # konversi ke uint8 jika float

    lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l_eq = clahe.apply(l)  # hanya L channel (grayscale)

    lab_eq = cv2.merge((l_eq, a, b))
    result = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2RGB)
    return result