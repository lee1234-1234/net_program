import socket
import struct
import random

def generate_data(request_type):
    if request_type == '1':
        temperature = random.randint(1, 50)
        humidity = 0
        light = 0
    elif request_type == '2':
        temperature = 0
        humidity = random.randint(1, 100)
        light = 0
    elif request_type == '3':
        temperature = 0
        humidity = 0
        light = random.randint(1, 150)
    else:
        temperature = 0
        humidity = 0
        light = 0
    return struct.pack('!HHH', temperature, humidity, light)

def main():
    server_address = ('localhost', 9999)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    print("UDP server is running...")

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            request_type = data.decode('utf-8')
            response = generate_data(request_type)
            server_socket.sendto(response, client_address)
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()