import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName

        # DNS Query Header 설정
        self.TransactionId = 1
        self.Flag = 0x0100  # 일반적인 질의 요청
        self.Questions = 1
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0

    def response(self, packet):  # DNS 응답 처리
        dnsHeader = packet[:12]
        dnsData = packet[12:].split(b'\x00', 1)

        # 응답의 Answer Resource Record 부분 추출
        ansRR = packet[12 + len(dnsData[0]) + 5 : 12 + len(dnsData[0]) + 21]
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)

        # IP 주소 디코딩 및 출력
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domainName, ip_addr)

    def query(self):  # DNS 질의 패킷 생성 및 전송
        # DNS Header 패킹
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query += struct.pack('!HH', self.Questions, self.AnswerRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        # 도메인 이름을 DNS 포맷으로 변환
        part = self.domainName.split('.')
        for i in range(len(part)):
            query += struct.pack('!B', len(part[i]))
            query += part[i].encode()
        query += b'\x00'  # 도메인 종료

        # Type A, Class IN 설정
        query_type = 1  # A 레코드
        query_class = 1  # IN 클래스
        query += struct.pack('!HH', query_type, query_class)

        # UDP 소켓 생성 및 전송
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ('8.8.8.8', 53)  # Google Public DNS
        sock.sendto(query, addr)

        # 응답 수신
        packet, address = sock.recvfrom(65535)
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = DnsClient(sys.argv[1])
        client.query()
