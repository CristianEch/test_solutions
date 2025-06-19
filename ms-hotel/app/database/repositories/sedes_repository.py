class SedesRepository():
    def __init__(self, table):
        self.table = table   


    
    async def get_sede_total_rooms(self, conn, ciudad):
        try:
            cursor = await conn.execute(f"""
        SELECT s.ciudad_sede, COUNT(h.id)
        FROM {self.table} AS s
        JOIN habitacion AS h
        ON s.id_sede  = h.sede
        GROUP BY s.ciudad_sede
        HAVING s.ciudad_sede = ?
        """,(ciudad,))
            row = await cursor.fetchone()
            return row
        except Exception as e:
            raise e
        


        