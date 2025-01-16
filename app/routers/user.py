from fastapi import APIRouter, Depends
from app.schemas import User, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router= APIRouter(
    prefix="/user",
    tags=["Users"]
)
usuarios= [] # esto es un dicionario cojone, no una lista

@router.get("/")
def obtener_usuarios(db:Session=Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return usuarios


@router.get("/ruta1")
def ruta1():
    return {"mensaje": "primmer commit"}


@router.get("/usuarios")
def getUsers():
    
   return usuarios

@router.get("/usuario/{id}")
def getUserByID(id:int):
    for usuario in usuarios:
        if usuario["id"]==id:
            print(usuario, type(user))
            return {"usuario": usuario}
    return{"Respuesta": "Usuario no encontrado"}
@router.delete("/delete/usuario/{id}")
def eliminar_usuario(id: int):
    # NECESITAMOS SABER EL INDICE Y EL VALOR PARA VER SI EL id = AL QUE ESTAMOS RECORRIENDO
    for index, user in enumerate(usuarios):
        if user["id"] == id:
            usuarios.pop(index)
            return {"Respuesta": "Usuario eliminado correctamente"}
    return {"Respuesta": "Usuario NO encontrado"}

@router.post("/crear_usuario")
def addUser(user: User):
    usuario= user.model_dump()
    usuarios.append(usuario)
    return {"Respuesta": "usuario creado!"}