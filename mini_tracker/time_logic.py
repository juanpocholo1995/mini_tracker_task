tiempo_total_acumulado = 0.0

def iniciar_tarea(tarea):
    print("Iniciando tarea:", tarea)

def detener_tarea(tiempo_trabajado):
    global tiempo_total_acumulado
    tiempo_total_acumulado += tiempo_trabajado
    print("Tiempo agregado:", tiempo_trabajado)

def consultar_total():
    return tiempo_total_acumulado