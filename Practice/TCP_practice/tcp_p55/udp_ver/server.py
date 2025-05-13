from socket import *

server = socket(AF_INET, SOCK_DGRAM)         # UDP 소켓 생성
server.bind(('', 9999))                      # 포트 9999 바인딩
print("UDP 서버 대기 중...")

data = b'This is IoT world!!!'
# 클라이언트로부터 초기 요청 수신
msg, client_addr = server.recvfrom(1024)

# 클라이언트에게 데이터를 여러 조각으로 전송 (4바이트씩)
for i in range(0, len(data), 4):
    chunk = data[i:i+4]
    server.sendto(chunk, client_addr)

server.close()
