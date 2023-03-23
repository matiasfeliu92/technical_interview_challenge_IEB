import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
sock.connect(server_address)
sock.send(b"GET / HTTP/1.1\r\nHost: /products/a04\r\n\r\n")
print('request send')
response = sock.recv(4096)
sock.close()
print(response)