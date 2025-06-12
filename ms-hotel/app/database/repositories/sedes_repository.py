class SedesRepository():
    def __init__(self, table):
        self.table = table   


    
    async def get_sede_total_rooms(self, conn, ciudad):
        try:
            cursor = await conn.execute(f"""SELECT SUM(num_hab_premium + num_hab_estandar + num_hab_vip)
            FROM {self.table} 
            WHERE ciudad_sede = ?""",(ciudad,))
            row = await cursor.fetchone()
            return row
        except Exception as e:
            raise e