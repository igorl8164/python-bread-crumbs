from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(b'this is testing', ('255.255.255.255', 10000))
while True:
    conn, addr = s.recvfrom(1024)
    print(addr)
