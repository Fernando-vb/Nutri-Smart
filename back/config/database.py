import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_db():
    """
    Función para obtener la instancia de la base de datos.
    Actualmente está configurada pero no se usa activamente hasta
    que se reemplace la lógica mock.
    """
    return db

# Ejemplo de cómo obtener una colección
# user_collection = db["users"]
