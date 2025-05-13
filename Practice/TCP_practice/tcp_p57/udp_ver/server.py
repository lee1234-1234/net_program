import socket
import cv2
import numpy as np
import time

BUF_SIZE = 1024
SERVER_PORT = 5005
VIDEO_FILE = 'test.mp4'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', SERVER_PORT))
print("UDP 서버 실행 중... 클라이언트 요청 대기")

client_addr = None
cap = cv2.VideoCapture(VIDEO_FILE)

while True:
    if client_addr is None:
        # 클라이언트의 시작 요청 대기
        data, addr = sock.recvfrom(1024)
        if data == b'start':
            client_addr = addr
            print(f"클라이언트 연결됨: {client_addr}")
        continue

    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 JPEG 인코딩
    result, img_encoded = cv2.imencode('.jpg', frame)
    byte_data = img_encoded.tobytes()
    total_size = len(byte_data)
    num_chunks = (total_size // BUF_SIZE) + 1

    # 먼저 전체 조각 수 전송
    sock.sendto(str(num_chunks).encode(), client_addr)

    # 프레임 데이터를 조각 내어 전송
    for i in range(num_chunks):
        start = i * BUF_SIZE
        end = start + BUF_SIZE
        chunk = byte_data[start:end]
        sock.sendto(chunk, client_addr)

    time.sleep(0.03)  # 약 30fps 속도
