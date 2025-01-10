from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    creacion_user: datetime = datetime.now()


    """
    Usuario de prueba:
    {
    "id": 1,
    "nombre": "jaime",
    "apellido": "gonzalez",
    "direccion": "mikasa",
    "telefono": 628182802,
    "creacion_user": "2025-01-09T13:19:05.357928"
}
    """