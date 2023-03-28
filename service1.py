import socket
import json

# Establecer la dirección IP y el puerto del servidor localhost
server_address = ('127.0.0.1', 8000)

# Crear un objeto de socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor localhost
sock.connect(server_address)

# Enviar la solicitud HTTP GET al servidor
request = "GET /products/a24 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\n\r\n"
sock.sendall(request.encode())

# Recibir la respuesta del servidor
response = ""
while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data)
    response += data.decode()


    # Extraer los datos JSON de la respuesta del servidor
    print(response)
    # json_data = response.split('\r\n\r\n')
    # parsed_data = json.loads(json_data)

    # Imprimir los datos JSON
    print(response)

    # Cerrar la conexión del socket
    sock.close()