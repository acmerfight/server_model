import threading
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

def server():
    HOST = "127.0.0.1"
    PORT = 9000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while 1:
        client_socket, _ = server_socket.accept()
        t = threading.Thread(target=handle_request, args=(client_socket, text_content))
        t.start()

def handle_request(client_socket, text_content):
    client_socket.recv(1024)
    try:
        print requests.get("http://www.amazon.com")
        client_socket.sendall(text_content)
    except socket.error:
        client_socket.close()
        return
    client_socket.close()


if __name__ == "__main__":
    server()
