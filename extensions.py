from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Membuat object database
db = SQLAlchemy()

# Membuat object login manager
login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.login_message = "Please login first."

login_manager.login_message_category = "warning"

# Halaman login jika user belum login
login_manager.login_view = "auth.login"

# Pesan ketika user belum login
login_manager.login_message = "Silakan login terlebih dahulu."

# Kategori pesan Bootstrap
login_manager.login_message_category = "warning"