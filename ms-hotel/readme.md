# 🏨 Microservicio MS-Hotel

Este proyecto es un microservicio desarrollado con **FastAPI** para la gestión de **habitaciones** y **sedes** hoteleras. Utiliza **SQLite** como base de datos local.

---

## 📁 Estructura del Proyecto

- `database/`: Conexión y configuración de la base de datos
- `dtos/`: Objetos de transferencia de datos (esquemas)
- `repositories/`: Consultas a la base de datos
- `routes/`: Rutas de la API (endpoints)
- `services/`: Lógica del negocio
- `main.py`: Punto de entrada principal

---

## ⚙️ Requisitos

- Python 3.10 o superior
- FastAPI
- Uvicorn

---

## 🚀 Cómo Ejecutar

1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/macOS
.venv\Scripts\activate     # En Windows