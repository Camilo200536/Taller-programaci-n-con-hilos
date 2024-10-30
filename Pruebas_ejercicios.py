import socket

# Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # Asignar IP y puerto
server_socket.listen(1)  # Permitir un cliente en espera

print("Servidor en espera de conexiones...")

while True:
    # Esperar conexión
    client_socket, client_address = server_socket.accept()
    print(f"Conexión desde: {client_address}")

    # Recibir datos
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Mensaje recibido: {data}")

    # Enviar respuesta
    response = "Mensaje recibido"
    client_socket.send(response.encode('utf-8'))

    # Cerrar conexión
    client_socket.close()