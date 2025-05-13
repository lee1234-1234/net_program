import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 9000)

# Send initial message to the server
sock.sendto(b"", server_addr)

# Receive message from the server
msg, _ = sock.recvfrom(1024)
print(msg.decode())

# Send "LTG" to the server
sock.sendto("LTG".encode(), server_addr)

# Receive student number from the server
data, _ = sock.recvfrom(4)
student_number = int.from_bytes(data, byteorder='big')
print(student_number)

sock.close()