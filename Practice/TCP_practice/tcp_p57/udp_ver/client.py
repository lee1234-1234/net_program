import socket
import cv2
import numpy as np

BUF_SIZE = 1024
SERVER_ADDR = ('localhost', 5005)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'start', SERVER_ADDR)  # 서버에 요청 보냄

while True:
    try:
        # 조각 개수 수신
        num_chunks, _ = sock.recvfrom(64)
        num_chunks = int(num_chunks.decode())

        byte_buffer = b''
        for _ in range(num_chunks):
            chunk, _ = sock.recvfrom(BUF_SIZE)
            byte_buffer += chunk

        # 바이트 -> numpy -> 이미지
        npdata = np.frombuffer(byte_buffer, dtype='uint8')
        img = cv2.imdecode(npdata, 1)
        if img is not None:
            cv2.imshow('UDP Image', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print("에러 발생:", e)
        break

sock.close()
cv2.destroyAllWindows()
