from fastapi import APIRouter, UploadFile, File, HTTPException
import cv2
import numpy as np
from app.model.load_model import session
from app.utils.embeding import get_embedding
from app.utils.face_crop import detect_and_align_face
from app.utils.match import match_face
from app.utils.lighting_normalisation import normalize_lighting
from app.utils.export_bas64 import encode_face_to_base64
from app.utils.preprocess import preprocess_face_for_embedding