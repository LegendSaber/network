from socket import *


tcpSerSock = socket(AF_INET, SOCK_STREAM)

ip_port = ('127.0.0.1', 6789)
tcpSerSock.bind(ip_port)
tcpSerSock.listen(5)

while True:
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = tcpCliSock.recv(1024)
  #  print(message)
  #  print(message.split()[1].partition("/")[2])
    filename = message.split()[1].partition("//")[2].replace('/', '_')
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        tcpCliSock.send("HTTP/1.1 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        tcpCliSock.sendall(outputdata)
        print("Read from cache.")
    except IOError:
        if fileExist == "false":
            c = socket(AF_INET, SOCK_STREAM)
            hostn = message.split()[1].partition("//")[2].partition("/")[0]
            print("Host Name: ", hostn)
            try:
                c.connect((hostn, 80))
                print("Socket connected to port 80 of the host")

                c.sendall(message.encode())

                buff = c.recv(4096)

                tcpCliSock.sendall(buff)
                tmpFile = open("./" + filename, "w")
                tmpFile.writelines(buff.decode().replace("\r\n", "\n"))
                tmpFile.close()
            except:
                print("Illegal request")
        else:
            tcpCliSock.send("HTTP/1.1 404 Not Found\r\n")
            print("File Not Found...")
    tcpCliSock.close()
tcpSerSock.close()

