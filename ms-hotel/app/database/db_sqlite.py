import aiosqlite
import logging

class DbSqlite():
    def __init__(self, dbPath: str):
        self._db_path = dbPath
        self._conn: aiosqlite.Connection | None = None
        
    async def connect(self) -> None:
        try:
            self._conn = await aiosqlite.connect(self._db_path)
            await self._conn.execute("PRAGMA journal_mode=WAL;")  # para mejor concurrencia
            await self._conn.execute("PRAGMA foreign_keys=ON;")    # asegurar integridad referencial
            logging.info("✅ Conexión a SQLite establecida.")
        except Exception as e:
            logging.error(f"❌ Error al conectar con SQLite: {e}")
            raise e

    async def acquireConnection(self):
        if not self._conn:
            raise Exception("Conexión no inicializada, llama a connect primero")
        await self._conn.execute('BEGIN;')
        return self._conn

    async def releaseConnection(self, conn):
        try:
            await conn.execute('ROLLBACK;')
        except Exception:
            pass  # Ya se hizo commit o rollback
        # En SQLite con aiosqlite no se "liberan" conexiones, ya que solo hay una

    async def commit(self, conn):
        await conn.execute('COMMIT;')

    async def closeConnection(self):
        if self._conn:
            await self._conn.close()
            self._conn = None
            logging.info("🔌 Conexión a SQLite cerrada correctamente.")