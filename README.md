# mini_tracker_task

Proyecto mínimo para rastrear tiempo de tareas.

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

```bash
[Iniciando tarea: 
Tiempo agregado: 2.5
Iniciando tarea: 
Tiempo agregado: 1.5
Tiempo total acumulado consultado: 4.0]

Si desea, puedo añadir descripciones más detalladas, ejemplos adicionales o corregir pequeños errores en el código (por ejemplo en `mini_tracker/__init__.py`).
