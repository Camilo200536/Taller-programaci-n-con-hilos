import socket

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect(('localhost', 8080))

# Enviar mensaje al servidor
mensaje = "Hola, servidor"
client_socket.send(mensaje.encode('utf-8'))

# Recibir respuesta del servidor
respuesta = client_socket.recv(1024).decode('utf-8')
print(f"Respuesta del servidor: {respuesta}")

# Cerrar la conexión
client_socket.close()