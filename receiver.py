import socket
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('115.145.242.44',10080))
while True:
    data, addr = sock.recvfrom(1472)

    print ('Server is received data : ', data.decode())
    print ('Send client ip : ', addr[0])
    print ('Send client port : ', addr[1])

