class TemporadaRepository():
    def __init__(self, table):
        self.table = table

    async def validate_season(self, conn, fecha_inicio: str):
        try:
            cursor = await conn.execute(f"""SELECT tipo
            FROM {self.table}
            WHERE ? >= fecha_inicio AND ? <= fecha_fin """, (fecha_inicio, fecha_inicio))
            row = await cursor.fetchone()
            print(f"-----------------------------------row-------------------------------------------------------------------------")
            return row
        except Exception as e:
            raise e
        

        