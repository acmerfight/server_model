import socket
import select
import time


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
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

inputs = [server_socket]
outputs = []
cnt = 1

while inputs:
    ready_to_read, ready_to_write, in_error = select.select(inputs, outputs, inputs)
    for s in ready_to_read:
        if s is server_socket:
            client_socket, addresss = server_socket.accept()
            client_socket.setblocking(0)
            inputs.append(client_socket)
        else:
            request = s.recv(1024)
            if request:
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

    for s in ready_to_write:
        time.sleep(1)
        s.sendall(text_content)
        outputs.remove(s)
        inputs.remove(s)
        s.close()

    for s in in_error:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
