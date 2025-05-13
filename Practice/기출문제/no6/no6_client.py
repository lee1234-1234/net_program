from socket import *
import time

port = 5555
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
server_addr = ('localhost', port)

while True:
    msg = input("Message to send (q to quit): ")
    if msg == 'q':
        break

    attempts = 0
    while attempts < 4:  # 최대 4회 전송
        sock.sendto(msg.encode(), server_addr)
        print(f"Sent attempt {attempts+1}")

        sock.settimeout(1.0)
        try:
            data, _ = sock.recvfrom(BUFFSIZE)
            if data.decode() == 'ack':
                print("ACK received!")
                break
        except timeout:
            print("No ACK, retrying...")
            attempts += 1

    if attempts == 4:
        print("Failed to receive ACK after 4 tries.")

sock.close()
