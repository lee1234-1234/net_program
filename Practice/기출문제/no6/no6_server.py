from socket import *
import random

port = 5555
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

print("UDP Echo Server is running...")

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received:', msg.decode())

    # 40% 확률로 손실 시뮬레이션
    if random.random() < 0.4:
        print("Packet lost (no ack sent)")
        continue

    # ack 전송
    sock.sendto(b'ack', addr)
    print("ACK sent.")
