import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9000))

while True:
    data, addr = s.recvfrom(1024)
    print('Connection from ', addr)
    s.sendto(b'Hello ' + addr[0].encode(), addr)

    name, addr = s.recvfrom(1024)
    print(name.decode())

    student_number = 20191542
    s.sendto(student_number.to_bytes(4, byteorder='big'), addr)