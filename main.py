from fastapi import FastAPI
import uvicorn

from model.user import User
# Esta comentado ya que he conseguido tener la implementacion del Usuario en otro fichero 
# De esta forma esta mas organizado.

"""from pydantic import BaseModel
from typing import Optional
from datetime import datetime"""

"""class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    creacion_user: datetime = datetime.now()"""


app = FastAPI()

usuarios= [] # esto es un dicionario cojone, no una lista


@app.get("/ruta1")
def ruta1():
    return {"mensaje": "primmer commit"}


@app.get("/usuarios")
def getUsers():
   if usuarios[0]==Null

@app.get("/usuario/{id}")
def getUserByID(id:int):
    for usuario in usuarios:
        if usuario["id"]==id:
            print(usuario, type(user))
            return usuario

@app.post("/crear_usuario")
def addUser(user: User):
    usuario= user.model_dump()
    usuarios.append(usuario)
    return {"Response": "User created!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
