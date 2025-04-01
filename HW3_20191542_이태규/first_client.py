import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = 'TAEGYU LEE'
sock.send(name.encode())

student_id_data = sock.recv(4)

student_id_data = struct.unpack("!I", student_id_data)[0]
print(student_id_data)

sock.close()