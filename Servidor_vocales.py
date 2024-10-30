import socket

def contar_vocales(cadena):
    # Cuenta las vocales en la cadena
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

def iniciar_servidor():
    # Configuración del servidor
    host = '127.0.0.1'  # Dirección local (localhost)
    puerto = 12345      # Puerto de escucha

    # Creación del socket del servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(5)  # Escucha hasta 5 conexiones simultáneas
    print("Servidor iniciado y esperando conexiones...")

    while True:
        # Acepta conexiones de clientes
        cliente, direccion = servidor.accept()
        print(f"Conexión establecida con {direccion}")

        # Recibe el mensaje del cliente
        cadena = cliente.recv(1024).decode('utf-8')
        print(f"Cadena recibida: {cadena}")

        # Procesa la cadena para contar las vocales
        num_vocales = contar_vocales(cadena)
        
        # Envía el número de vocales de vuelta al cliente
        respuesta = f"El número de vocales en la cadena es: {num_vocales}"
        cliente.send(respuesta.encode('utf-8'))

        # Cierra la conexión con el cliente
        cliente.close()
        print("Conexión cerrada con el cliente.")

if __name__ == "__main__":
    iniciar_servidor()