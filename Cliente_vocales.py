import socket

def enviar_cadena(cadena):
    host = '127.0.0.1' 
    puerto = 12345     

    # Creación del socket del cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))

    # Enviar la cadena al servidor
    cliente.send(cadena.encode('utf-8'))

    # Recibir la respuesta del servidor
    respuesta = cliente.recv(1024).decode('utf-8')
    print(respuesta)

    # Cerrar la conexión
    cliente.close()

if __name__ == "__main__":
    cadena = input("Ingresa una cadena para contar las vocales: ")
    enviar_cadena(cadena)