import socket as soc

s = soc.socket()
s.bind(('localhost', 9999))
s.listen(3)

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected To ", name, addr)

    c.send(bytes('Welcome to socket programming', 'utf-8'))
    c.close()

