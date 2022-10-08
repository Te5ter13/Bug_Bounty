import socket

#1. socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2. bind
s.bind(("127.0.0.1",1234)) #in tuple

#3. listen
s.listen(5)

#4. accept
client,address=s.accept()
print(address)
#5. Receive
msg = client.recv(2048).decode()
print(msg)

#6. send
client.send("Hello I am Server".encode())

client.close()
s.close()
