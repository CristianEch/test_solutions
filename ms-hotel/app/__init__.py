import logging
from fastapi import FastAPI
from app.view import get_api_router



logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
)

app = FastAPI(
    title="Cadena Hoteles Axede",
    description=(
        "descripcion"
    ),
    version="0",
    contact={
        "name": "nombre",
        "email": "correog@gmail.com",
    },
    openapi_url="/openapi.json", 
    docs_url="/swagger",  
    redoc_url="/redocs",
)

@app.get("/")
def default():
    return {"message":"hello mundo"}


app.include_router(get_api_router())
