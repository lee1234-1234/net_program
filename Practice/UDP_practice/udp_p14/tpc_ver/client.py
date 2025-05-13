from socket import *
import random

PORT = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', PORT)
sock.connect(addr)  # Establish a connection to the server

while True:
    msg = input('>> ')
    reTx = 0
    while reTx <= 5:  # 최대 5회까지 재전송
        resp = msg + f' ({str(reTx)} tried)'
        sock.send(resp.encode())
        sock.settimeout(2)
        try:
            data = sock.recv(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 3:
        print('Timeout.')

    sock.settimeout(None)
    while True:
        data = sock.recv(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.send(b'ack')
            print('[Server] :', data.decode())
            break

sock.close()