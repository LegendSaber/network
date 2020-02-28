from socket import *
import time

clientServer = socket(AF_INET, SOCK_DGRAM)
clientServer.settimeout(1)
ip_port = ('127.0.0.1', 12000)

count = 1
while count <= 10:
    beginTime = time.time()
    message = ("Ping %d %s" % (count, beginTime))
    try:
        clientServer.sendto(message.encode('utf-8'), ip_port)
        result, serverAddr = clientServer.recvfrom(1024)
        rtt = time.time() - beginTime
        print("Sequence %d: Reply from %s RTT = %.3fs" % (count, serverAddr, rtt))
    except Exception as e:
        print('Sequence %d: Request timed out' % (count))
    count = count + 1
clientServer.close()