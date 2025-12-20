## ⏱️ Mini Tracker Task
Un proyecto mínimo en Python para rastrear el tiempo de tareas. Su objetivo es servir como ejemplo didáctico de cómo estructurar un paquete simple que permita iniciar, detener y consultar tiempos acumulados de actividades.
Proyecto mínimo para rastrear tiempo de tareas.

## 📂 Estructura del proyecto

```
mini_tracker_task/
│
├── main.py                # Script de ejemplo que demuestra el flujo básico
├── mini_tracker/          # Paquete principal con la lógica de tiempo
│   ├── __init__.py        # Inicializador del paquete y funciones públicas
│   └── time_logic.py      # Implementación de la lógica de tiempo
├── historial              # Registro de actividad impreso en consola
├── LICENSE                # Licencia MIT
└── README.md              # Documentación del proyecto
```
## 🚀 Instalación y uso
Clona el repositorio:

```
git clone https://github.com/juanpocholo1995/mini_tracker_task.git
cd mini_tracker_task
```

## Ejecuta el script de ejemplo:
```
python3 main.py
```

## Archivos del proyecto

- `LICENSE`: Archivo de licencia del proyecto.
- `main.py`: Script de ejemplo que importa el paquete `mini_tracker` y demuestra el flujo básico: iniciar una tarea, detenerla y consultar el tiempo total acumulado. Contenido actual:

```
from mini_tracker import iniciar_tarea, detener_tarea, consultar_total
iniciar_tarea("")
detener_tarea(2.5)
iniciar_tarea("")
detener_tarea(1.5)
print("Tiempo total acumulado consultado:", consultar_total())
```

- `mini_tracker/__init__.py`: Inicializador del paquete. Expone las funciones públicas `iniciar_tarea`, `detener_tarea` y `consultar_total`, y define `__version__`.
- `mini_tracker/time_logic.py`: Implementa la lógica de tiempo. Contiene una variable `tiempo_total_acumulado` y funciones para iniciar y detener tareas, y para consultar el total.
- `mini_tracker/__pycache__/`: Carpeta de caché generada por Python (archivos .pyc).

## Uso

Importar desde el paquete y usar las funciones expuestas:

```
from mini_tracker import iniciar_tarea, detener_tarea, consultar_total

iniciar_tarea("Mi tarea")
detener_tarea(1.25)
print(consultar_total())

```
# Mini Tracker Task

### Registro de Actividad (Consola impresion):
<img width="725" height="280" alt="image" src="https://github.com/user-attachments/assets/66bad2f8-bc73-4662-a4be-c05db1462905" />

```
[Iniciando tarea: 
Tiempo agregado: 2.5
Iniciando tarea: 
Tiempo agregado: 1.5
Tiempo total acumulado consultado: 4.0]
