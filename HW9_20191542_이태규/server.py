import socket, select
import time

socks = []
BUF_SIZE = 1024
PORT = 1234

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print('Server Started')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            conn, addr = s_sock.accept()
            socks.append(conn)
            print(f'New Client {addr} connected.')
        else:
            data = s.recv(BUF_SIZE)

            if 'quit' in data.decode():
                print(addr, 'exited')
                socks.remove(s)
                s.close()
                continue

            print(time.asctime() + str(addr) + ':' + data.decode())

            for client in socks:
                if client != s and client != s_sock:
                    client.send(data)