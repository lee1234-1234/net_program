from socket import *

BUF_SIZE = 1024
port = 4321

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

mbox = {}

while True:
    data, addr = s_sock.recvfrom(BUF_SIZE)
    msg = data.decode() 

    if msg == 'quit':
        break

    elif msg.startswith('send'):
        _, mboxid, *message = msg.split()
        message = ' '.join(message)

        if mboxid not in mbox:
            mbox[mboxid] = []
            
        mbox[mboxid].append(message)
        s_sock.sendto(b"OK", addr)

    elif msg.startswith('receive'):
        _, mboxid = msg.split()
        if mboxid in mbox and mbox[mboxid]:
            rep = mbox[mboxid].pop(0)
            s_sock.sendto(rep.encode(), addr)
        else:
            s_sock.sendto(b'No messages', addr)
            
s_sock.close()