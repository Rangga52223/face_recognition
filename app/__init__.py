from fastapi import FastAPI
from app.route.face_route import router as face_router
from app.db_model.database import Base, engine

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Face Recognition Identifier API",
    version="1.0.0",
    description="App to identify face from image/video by Rangga Wahyu Nugroho",
)

app.include_router(face_router)
