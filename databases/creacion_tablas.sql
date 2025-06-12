CREATE TABLE IF NOT EXISTS sede (
    id_sede INTEGER PRIMARY KEY AUTOINCREMENT,
    ciudad_sede TEXT NOT NULL,
    num_hab_premium INTEGER DEFAULT 0 CHECK (num_hab_premium >= 0),
    num_hab_estandar INTEGER DEFAULT 0 CHECK (num_hab_estandar >= 0),
    num_hab_vip INTEGER DEFAULT 0 CHECK (num_hab_vip >= 0),
    cupo_max_habitacion INTEGER NOT NULL CHECK (cupo_max_habitacion > 0 AND cupo_max_habitacion < 9),
    precio_base_por_dia REAL NOT NULL CHECK (precio_base_por_dia >= 0)
);

-- Table: habitacion
CREATE TABLE IF NOT EXISTS habitacion (
    id_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
    sede_habitacion INTEGER NOT NULL,
    tipo_habitacion TEXT NOT NULL CHECK (tipo_habitacion IN ('premium', 'estandar', 'vip')),
    estado TEXT NOT NULL CHECK (estado IN ('ocupada', 'no ocupada')), -- voy a borrar este estado
    fecha_inicio TEXT,  -- ISO 8601 format: YYYY-MM-DD
    fecha_final TEXT,
    cliente INTEGER,
    FOREIGN KEY (sede_habitacion) REFERENCES sede(id_sede) ON DELETE CASCADE,
    FOREIGN KEY (cliente) REFERENCES cliente(id_cliente) ON DELETE SET NULL
);