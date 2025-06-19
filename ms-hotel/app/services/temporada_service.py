import logging
from app.database.db_sqlite import DbSqlite
from app.database.repositories.temporada_repository import TemporadaRepository

class TemporadaService():
    def __init__(self):
        self.path = "/home/cristian/Documents/programming/prueba_axede_cristian/databases/cadena-hoteles.db"
        self.db = DbSqlite(dbPath = self.path)
        self.repository = TemporadaRepository(table = "temporada")
    
    async def get_season(self, fecha):
        try:
            await self.db.connect()
            conn = await self.db.acquireConnection()
            season = await self.repository.validate_season(conn = conn, fecha_inicio=fecha)
            logging.info(season)
            if season == None:
                return "Baja"
            else:
                return season[0]
        except Exception as e:
            logging.error(f"************Error en temporada service: {e}")
            raise e
        finally:
            await self.db.closeConnection()