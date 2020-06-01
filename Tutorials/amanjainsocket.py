import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost", 9999))

s.listen(3)

print("Waiting for connection")

while True:
    c, addre = s.accept()
    print("Client Connected", addre)
    name = (c.recv(1024).decode())
    print(name)
    c.send(bytes("Welcome to Python","utf-8"))

    c.close()