from fastapi import APIRouter, Depends
from app.schemas import User, UserId, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router= APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/", response_model=List[ShowUser])
def getUsers(db:Session=Depends(get_db)):
    data = db.query(models.User).all()
    return data

@router.get("/{id}", response_model=ShowUser)
def getUserByID(id:int, db:Session=Depends(get_db)):
    usuario= db.query(models.User).filter(models.User.id==id).first()
    if not usuario:
        return {"Respuesta": "Usuario no encontrado."}
    else:
        return usuario

@router.delete("/{id}/delete")
def eliminar_usuario(id: int, db:Session=Depends(get_db)):
    usuario= db.query(models.User).filter(models.User.id==id).first()
    if not usuario:
        return {"Respuesta": "Usuario no encontrado."}
    else:
        db.delete(usuario)
        db.commit()
        return {"Respuesta": "Usuario eliminado con exito."}

@router.patch("/{id}")
def modificar_usuario(id: int, updateUser: UpdateUser, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id==id)
    if not usuario.first():
        return {"Respuesta": "Usuario no encontrado."}
    usuario.update(updateUser.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Usuario modificado con exito."}

@router.post("/crear_usuario")
def addUser(user: User, db:Session=Depends(get_db)):
    usuario= user.model_dump()
    nuevo_usuario= models.User(
        username = usuario["username"],
        password = usuario["password"],
        nombre = usuario["nombre"],
        apellido = usuario["apellido"],
        direccion = usuario["direccion"],
        telefono = usuario["telefono"],
        correo = usuario["correo"],
    )
    data = db.query(models.User).all()
    existe= False
    for dataUser in data:
        # print("usuario data"+str(dataUser.username)) asi si joe
        if dataUser.username == nuevo_usuario.username:
            existe=True
    if existe:
        return {"Respuesta": "error al crear usuario."}
    else: 
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return {"Respuesta": "usuario creado!"}