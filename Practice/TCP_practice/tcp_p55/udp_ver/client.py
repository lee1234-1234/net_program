from socket import *

sock = socket(AF_INET, SOCK_DGRAM)                # UDP 소켓 생성
server_addr = ('localhost', 9999)

# 서버에 "시작" 요청을 보내서 응답 유도
sock.sendto(b'start', server_addr)

data_size = 20
rx_size = 0
total_data = []

while rx_size < data_size:
    data, _ = sock.recvfrom(1024)                # 전체 패킷 수신
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)

message = ''.join(total_data)
print(message)

sock.close()
