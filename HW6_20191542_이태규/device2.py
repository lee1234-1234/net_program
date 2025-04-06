import socket
import random

def run_device2():
    # 디바이스 2: 심박수, 걸음수, 소모 칼로리 데이터를 제공 (포트 9002)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9002))
    s.listen(5)
    print("Device2 (심박수, 걸음수, 소모 칼로리) 서버 시작됨, 포트 9002")
    
    while True:
        c, addr = s.accept()
        print("Device2: 연결 요청 from", addr)
        data = c.recv(1024).decode().strip()
        if not data:
            c.close()
            continue
        
        print("Device2: 받은 메시지:", data)
        if data == "Request":
            # 심박수: 40~140, 걸음수: 2000~6000, 소모칼로리: 1000~4000
            heartbeat = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)
            response = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
            c.send(response.encode())
        elif data == "quit":
            print("Device2: 종료 명령 수신, 서버 종료")
            c.send("Device2 종료".encode())
            c.close()
            break
        c.close()
    s.close()

if __name__ == '__main__':
    run_device2()
