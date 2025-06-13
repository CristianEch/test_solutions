WITH RECURSIVE cnt(x) AS (
  SELECT 1
  UNION ALL
  SELECT x + 1 FROM cnt WHERE x < 19
)
INSERT INTO habitacion (sede_habitacion, tipo_habitacion)
SELECT 1, 'estandar' FROM cnt;