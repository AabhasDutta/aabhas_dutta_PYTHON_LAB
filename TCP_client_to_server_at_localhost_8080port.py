import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8080))

print("Connected to server")

client.close()