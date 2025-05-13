import socket

port = 2500
BUFFSIZE = 1024

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

print(f"TCP server is running on port {port}...")

while True:
    # Accept a connection from a client
    conn, addr = sock.accept()
    print('Connected by', addr)
    
    while True:
        # Receive message from client
        msg = conn.recv(BUFFSIZE)
        if not msg:
            break
        print('Received from', addr, ':', msg.decode())
        
        # Echo the message back to the client
        conn.send(msg)
    
    # Close the connection
    conn.close()