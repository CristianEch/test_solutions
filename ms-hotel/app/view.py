from fastapi import APIRouter

from app.routes import sede_routes
from app.routes import habitacion_routes
from app.routes import temporada_routes


api_router = APIRouter()

api_router.include_router(sede_routes.router)

api_router.include_router(habitacion_routes.router)

api_router.include_router(temporada_routes.router)




def get_api_router():
    return api_router