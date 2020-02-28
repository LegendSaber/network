#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen(5)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\n' \
                     'Connection: close\n' \
                     'Content-Type: text/html\n' \
                     'Content-Length: %d \n\n' % len(outputdata)
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()
    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        connectionSocket.close()

serverSocket.close()
