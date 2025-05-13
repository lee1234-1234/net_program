from socket import *
import random
import time

PORT = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', PORT)
while True:
    msg = input('>> ')
    reTx = 0
    while reTx <= 5:  # 최대 5회까지 재전송
        resp = msg + f' ({str(reTx)} tried)'
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 3:
        print('Timeout.')

    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('[Server] :', data.decode())
            break