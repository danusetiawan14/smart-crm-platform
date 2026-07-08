import os
from dotenv import load_dotenv

# Membaca file .env
load_dotenv()


class Config:
    """Konfigurasi utama aplikasi."""

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False