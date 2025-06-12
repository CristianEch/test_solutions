from fastapi import APIRouter
from datetime import date


router = APIRouter()

@router.get("/haabitacion")
async def habitacion_route():
    return {"message":"hola prueba"}