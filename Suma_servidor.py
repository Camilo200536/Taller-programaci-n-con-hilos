import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345        # Puerto de escucha del servidor

# Crear el socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Servidor en espera de conexiones...")

    # Aceptar la conexión del cliente
    conn, addr = server_socket.accept()
    with conn:
        print(f"Conectado por {addr}")
        
        suma = 0
        while True:
            # Recibir el número enviado por el cliente
            data = conn.recv(1024)
            if not data:
                break

            # Convertir los datos recibidos a un número entero
            numero = int(data.decode())
            print(f"Número recibido: {numero}")

            # Si el número es cero, envía la suma acumulada y reinicia la suma
            if numero == 0:
                conn.sendall(str(suma).encode())
                print(f"Enviando suma: {suma}")
                suma = 0  # Reiniciar la suma para nuevas conexiones
            else:
                suma += numero  # Sumar el número recibido