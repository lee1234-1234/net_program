import socket
import struct
import random

def generate_random_data():
    sender_id = random.randint(1, 50000)
    receiver_id = random.randint(1, 50000)
    light = random.randint(1, 100)
    humidity = random.randint(1, 100)
    temperature = random.randint(1, 100)
    pressure = random.randint(1, 100)
    sequence_number = random.randint(1, 100000)
    return sender_id, receiver_id, light, humidity, temperature, pressure, sequence_number

def main():
    server_address = ('localhost', 5050)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)

        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data == 'Hello':
                random_data = generate_random_data()
                packed_data = struct.pack('!H H B B B B I', *random_data)
                client_socket.sendall(packed_data)
        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()