import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost para pruebas locales)
PORT = 12345        # Mismo puerto que el servidor

# Crear el socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Ejemplo de números para enviar
    numeros = [5, 10, 15, 0]  # El último número debe ser 0 para recibir la suma

    for numero in numeros:
        # Enviar número al servidor
        client_socket.sendall(str(numero).encode())
        print(f"Número enviado: {numero}")
        
        # Si enviamos un cero, esperamos la respuesta del servidor
        if numero == 0:
            data = client_socket.recv(1024)
            suma = int(data.decode())
            print(f"Suma recibida del servidor: {suma}")