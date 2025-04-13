import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(BASE_DIR, "database")  # Diretório do banco de dados
DATABASE_PATH = os.path.join(DATABASE_DIR, "calendar_database.sqlite3")

# Certifique-se de que o diretório do banco de dados existe
os.makedirs(DATABASE_DIR, exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Debug: Verificar os caminhos
print(f"Database directory: {DATABASE_DIR}")
print(f"Database path: {DATABASE_PATH}")
print(f"SQLAlchemy database URL: {SQLALCHEMY_DATABASE_URL}")