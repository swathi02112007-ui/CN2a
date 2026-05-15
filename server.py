import socket
s=socket.socket()
s.connect(('localhost',7000))
while True:
    print(s.recv(1024).decode())
    s.send("Acknowledgement Received".encode())