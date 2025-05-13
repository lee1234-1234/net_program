from socket import *
import argparse

# Create a socket
s = socket(AF_INET, SOCK_STREAM)

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-s', default='localhost', help='Server address')
parser.add_argument('-p', type=int, default=2500, help='Port number')
args = parser.parse_args()

# Connect to the server
s.connect((args.s, args.p))
print('Connected to', args.s, args.p)

# Communication loop
while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    if not data:
        break
    print('Received message:', data.decode())

# Close the socket
s.close()