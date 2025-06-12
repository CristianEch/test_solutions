from fastapi import APIRouter
from app.services.sede_service import SedesService
from app.dtos.sede_dto import TotalRoomsSede


router = APIRouter()

@router.get("/total_hab_ciudad/{ciudad}")
async def total_hab_sede(ciudad: str):
    service = SedesService()
    total = await service.get_total_rooms(ciudad)
    return TotalRoomsSede(total_rooms_sede=total)