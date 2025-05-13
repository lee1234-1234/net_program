from socket import *

s = socket(AF_INET, SOCK_DGRAM)

server_address = ('localhost', 3333)

while True:
    msg = input('Enter expression: ')
    if msg.lower() == 'q':
        s.sendto(msg.encode(), server_address)
        break
    
    s.sendto(msg.encode(), server_address)
    result, _ = s.recvfrom(1024)
    print('Result:', result.decode())

s.close()