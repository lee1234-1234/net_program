import socket
import random

def run_device1():
    # 디바이스 1: 온도, 습도, 조도 데이터를 제공 (포트 9001)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9001))
    s.listen(5)
    print("Device1 (온도, 습도, 조도) 서버 시작됨, 포트 9001")
    
    while True:
        c, addr = s.accept()
        print("Device1: 연결 요청 from", addr)
        data = c.recv(1024).decode().strip()
        if not data:
            c.close()
            continue
        
        print("Device1: 받은 메시지:", data)
        if data == "Request":
            # 온도: 0~40, 습도: 0~100, 조도: 70~150 (임의의 정수 생성)
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            illum = random.randint(70, 150)
            response = f"Temp={temp}, Humid={humid}, Illum={illum}"
            c.send(response.encode())
        elif data == "quit":
            print("Device1: 종료 명령 수신, 서버 종료")
            c.send("Device1 종료".encode())
            c.close()
            break
        c.close()
    s.close()

if __name__ == '__main__':
    run_device1()
