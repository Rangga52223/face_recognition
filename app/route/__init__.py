from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db_model.face_save import FaceSave
from app.depencies.session import get_db
from app.face_proses.face_re import register_face_re, recognition_face_re, delete_face_re, get_all_face

router = APIRouter(
    prefix="/api/face",
    tags=["face"]
)