import socket
import select


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
    ready_to_read, ready_to_write, in_error = select.select([server_socket], [], [], 5)
    for s in ready_to_read:
        if s is server_socket:
            client_socket, addresss = server_socket.accept()
            #client_socket.setblocking(0)
            request = client_socket.recv(1024)
            try:
                client_socket.sendall(text_content)
            except socket.error:
                client_socket.close()
            client_socket.close()
