import socket

port = 2500
BUFFSIZE = 1024

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print(f"UDP server is running on port {port}...")

while True:
    # Receive message from client
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received from', addr, ':', msg.decode())
    
    # Echo the message back to the client
    sock.sendto(msg, addr)