import argparse
import socket
import random
from datetime import datetime

BUFF_SIZE = 1024

def Server(ipaddr, port):  # 서버 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print('Waiting in {}...'.format(sock.getsockname()))
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() < prob:
            print('Message from {} is lost.'.format(addr))
            continue
        print('{} client message {!r}'.format(addr, data.decode()))
        text = 'The length is {} bytes.'.format(len(data))
        sock.sendto(text.encode(), addr)

def Client(hostname, port):  # 클라이언트 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    index = 1  # 보낸 메시지 번호
    time = 0.1  # seconds
    while True:
        data = str(datetime.now())
        sock.sendto(data.encode(), (hostname, port))
        print('({}) Waiting for {} sec'.format(index, time))
        sock.settimeout(time)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:
            time *= 2
            if time > 2.0:
                print('{}th packet is lost'.format(index))
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1
            else:
                continue
        else:
            print('Server reply: {!r}'.format(data.decode()))
            if index >= sending_counts:
                break
            index += 1
            time = 0.1

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}
    parser = argparse.ArgumentParser(description='Send and receive UDP packets with setting drop probability')
    parser.add_argument('role', choices=mode, help='which role to take between server and client')
    parser.add_argument('-s', default='localhost', help='server that client sends to')
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)')
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)')
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')
    args = parser.parse_args()

    prob = args.prob
    sending_counts = args.count

    if args.role == 'c':
        mode[args.role](args.s, args.p)
    else:
        mode[args.role]('', args.p)