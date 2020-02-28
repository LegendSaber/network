from socket import *
import base64

mailserver = "smtp.qq.com"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'HELO 1900\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')

clientSocket.sendall('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
    print('334 reply not received from server')

fromAddress = "747671402@qq.com"
username = base64.b64encode(fromAddress.encode()).decode()
clientSocket.sendall((username + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '334':
    print('334 reply not received from server')

password = base64.b64encode("evcqqmijetvgbdfh".encode()).decode()
clientSocket.sendall((password + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
    print('235 reply not received from server')

clientSocket.sendall(('MAIL FROM: <' + fromAddress + '>\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')

toAddress = "747671402@qq.com"
clientSocket.sendall(('RCPT TO: <' + toAddress + '>\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')

clientSocket.sendall('DATA\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '354':
    print('354 reply not received from server')

subject = "I love computer netword"
contenttype = "text/plain"
msg = "\r\n I Love computer networks!"
message = 'From:' + fromAddress + '\r\n'
message += 'To:' + toAddress + '\r\n'
message += 'Subject: ' + subject + '\r\n'
message += 'Content-type:' + contenttype + '\t\n'
message += '\r\n' + msg
clientSocket.sendall(message.encode())

endmsg = "\r\n.\r\n"
clientSocket.sendall(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')

clientSocket.sendall('QUIT\r\n'.encode())

clientSocket.close()