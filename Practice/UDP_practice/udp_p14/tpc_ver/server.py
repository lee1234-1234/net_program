from socket import *
import random

PORT = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(1)

print("Waiting for a client...")
conn, addr = sock.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(BUFF_SIZE)
    if not data:
        break

    if random.random() <= 0.5:
        continue
    else:
        conn.send(b'ack')
        print('[Client] :', data.decode())

    msg = input('>> ')
    reTx = 0
    while reTx <= 5:  # 최대 5회까지 재전송
        resp = msg + f' ({str(reTx)} tried)'
        conn.send(resp.encode())

        try:
            conn.settimeout(2)
            data = conn.recv(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 3:
        print('Timeout.')

conn.close()
sock.close()