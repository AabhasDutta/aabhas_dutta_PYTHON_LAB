import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080))

server.listen(1)

print("Server is waiting...")

conn, addr = server.accept()

data = conn.recv(1024)

print("Received:", data.decode())

conn.send("Message received".encode())

conn.close()
server.close()