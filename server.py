import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080))

server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()

print("Client connected:", addr)

conn.close()
server.close()