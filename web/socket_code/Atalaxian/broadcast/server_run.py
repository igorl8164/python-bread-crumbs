from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 10000))
while True:
    conn, addr = s.recvfrom(4096)
    print(addr)
    s.sendto(b'message received by the server', addr)
