import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
videoFile = 'test.mp4'  # Video file in the current folder. Provide the full path if it's in a different location.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(5)

while True:
    csock, addr = sock.accept()
    print('Client is connected')
    cap = cv2.VideoCapture(videoFile)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            temp = csock.recv(BUF_SIZE)  # Receive 'start'
            if not temp:
                break
            result, imgEncode = cv2.imencode('.jpg', frame)
            data = np.array(imgEncode)
            byteData = data.tobytes()
            csock.send(str(len(byteData)).zfill(LENGTH).encode())  # Send length as a 10-character string
            temp = csock.recv(BUF_SIZE)  # Receive 'image'
            if not temp:
                break
            csock.send(byteData)  # Send image data
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    csock.close()