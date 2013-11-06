import socket
import time
import requests


text_content = """
HTTP/1.x 200 OK
Content-Type: text/html

<head>
    <title>WOW</title>
</head>
<html>
    <p>Hello World!</p>
</html>
"""

HOST = "127.0.0.1"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while 1:
    client_socket, addresss = server_socket.accept()
    request = client_socket.recv(1024)
    try:
        requests.get("http://www.amazon.com")
        client_socket.sendall(text_content)
    except socket.error:
        client_socket.close()
    client_socket.close()
