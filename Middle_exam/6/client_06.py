import socket
import struct


def main():
    server_address = 'localhost'
    server_port = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((server_address, server_port))
            client_socket.sendall(b'Hello')
            data = client_socket.recv(12)
            if len(data) == 12:
                sender_id, receiver_id, light, humidity, temperature, pressure, sequence_number = struct.unpack('>H H B B B B I', data)
                
                print(f"Sender: {sender_id}, Receiver: {receiver_id}, Lumi: {light}, Humi: {humidity}, Temp: {temperature}, Air: {pressure}, Seq: {sequence_number}")
            else:
                print("올바르지 않은 데이터")
        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()