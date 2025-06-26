class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Rangga%40%29%29%40312@host.docker.internal:5432/db_face_recognition'
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'pool_size': 5,
        'max_overflow': 5,
        'pool_timeout': 30
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
