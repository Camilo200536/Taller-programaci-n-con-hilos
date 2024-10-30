import psutil

def listar_procesos():
    print("Lista de procesos:")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"PID: {proc.info['pid']} - Nombre: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def eliminar_proceso(pid):
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()  # Envía señal de terminación al proceso
        proceso.wait()       # Espera a que el proceso se cierre
        print(f"Proceso con PID {pid} terminado exitosamente.")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print("No se pudo terminar el proceso. Verifique el PID y los permisos.")

if __name__ == "__main__":
    listar_procesos()
    try:
        pid = int(input("\nIngrese el PID del proceso que desea eliminar: "))
        eliminar_proceso(pid)
    except ValueError:
        print("Por favor, ingrese un número de PID válido.")



        