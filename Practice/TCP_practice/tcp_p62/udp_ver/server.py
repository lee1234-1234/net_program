from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4  # 파일 크기 4바이트

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 7777))
print('UDP File Server is running...')

while True:
    msg, client_addr = sock.recvfrom(BUF_SIZE)
    if msg != b'Hello':
        print('Invalid hello from', client_addr)
        continue
    print('Client connected:', client_addr)
    
    sock.sendto(b'Filename', client_addr)

    msg, client_addr = sock.recvfrom(BUF_SIZE)
    filename = msg.decode()
    print('Client requested:', filename)

    try:
        filesize = os.path.getsize(filename)
    except:
        sock.sendto(b'Nofile', client_addr)
        continue

    # 파일 크기를 4바이트 big-endian으로 인코딩해서 전송
    fs_binary = filesize.to_bytes(LENGTH, 'big')
    sock.sendto(fs_binary, client_addr)

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sock.sendto(data, client_addr)

    # 완료 메시지 수신
    msg, _ = sock.recvfrom(BUF_SIZE)
    if msg == b'Bye':
        print('Transfer complete from', client_addr)
