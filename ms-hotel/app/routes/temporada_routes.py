from fastapi import APIRouter, Query
from app.services.temporada_service import TemporadaService
from app.dtos.temporada_dto import tipo_temporada

router = APIRouter()

@router.get("/temporada")
async def get_temporada(inicio: str = Query(..., description="Fecha de inicio (YYYY-MM-DD)")):
    
    service = TemporadaService()
    response = await service.get_season(fecha=inicio)
    return response