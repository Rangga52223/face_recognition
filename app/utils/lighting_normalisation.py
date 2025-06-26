import cv2
import numpy as np

def normalize_lighting(image: np.ndarray) -> np.ndarray:
    """
    Input: RGB image (112,112,3)
    Output: RGB image setelah normalisasi pencahayaan
    """
    lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l_eq = clahe.apply(l)

    lab_eq = cv2.merge((l_eq, a, b))
    result = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2RGB)
    return result