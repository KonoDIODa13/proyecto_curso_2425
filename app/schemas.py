from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    #id: int
    username: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    creacion_user: datetime = datetime.now()

class UserId(BaseModel):
    id:int


class ShowUser(BaseModel):
    username: str
    nombre:str
    correo:str


class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    nombre: str = None
    apellido: str = None
    direccion: str = None
    telefono: int = None
    correo: str = None

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