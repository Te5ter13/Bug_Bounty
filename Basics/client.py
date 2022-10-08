import socket

#1. socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2. connect
c.connect(("127.0.0.1",1234))

#3. send
c.send("Hello I am Client".encode())

#4. recv
msg = c.recv(2048).decode()
print(msg)

c.close()
