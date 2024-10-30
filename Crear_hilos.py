import threading
import random

# Función que será ejecutada por cada hilo
def sumar_numeros(hilo_id, resultados):
    suma = sum(random.randint(1, 1000) for _ in range(100))
    print(f"Hilo {hilo_id}: suma total = {suma}")
    resultados[hilo_id] = suma  # Guardamos el resultado en un diccionario

def main():
    resultados = {}
    hilos = []

    # Crear y ejecutar los 10 hilos
    for i in range(1, 11):
        hilo = threading.Thread(target=sumar_numeros, args=(i, resultados))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Determinar el hilo con el mayor resultado
    hilo_ganador = max(resultados, key=resultados.get)
    print(f"\nHilo ganador: {hilo_ganador} con una suma de {resultados[hilo_ganador]}")

if __name__ == "__main__":
    main()