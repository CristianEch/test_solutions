import logging
from app.database.db_sqlite import DbSqlite
from app.database.repositories.sedes_repository import SedesRepository


class SedesService():
    def __init__(self):
        self.path = "/home/cristian/Documents/programming/prueba_axede_cristian/databases/cadena-hoteles.db"
        self.db = DbSqlite(dbPath = self.path)
        self.repository = SedesRepository(table="SEDE")


    async def get_total_rooms(self, ciudad):
        
        try:
            await self.db.connect()
            conn = await self.db.acquireConnection()
            row = await self.repository.get_sede_total_rooms(conn=conn, ciudad=ciudad)
            
            await self.db.commit(conn=conn)
            
            return row[0]
        except Exception as e:
            logging.error(f"Error en sedes_service: {e}")
            raise e
        finally:
            await self.db.closeConnection()