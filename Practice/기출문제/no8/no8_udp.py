import socket

# Relay server configuration
RELAY_HOST = 'localhost'
RELAY_PORT = 9000

# Target server configuration
TARGET_HOST = 'www.daum.net'
TARGET_PORT = 80

def handle_client(data, client_address, server_socket):
    try:
        print("Received request from client:")
        print(data.decode('utf-8'))

        # Create a new socket to connect to the target server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as target_socket:
            target_socket.connect((TARGET_HOST, TARGET_PORT))

            # Forward the received data to the target server
            target_socket.sendall(data)

            # Receive the HTTP response from the target server
            response = b""
            while True:
                chunk = target_socket.recv(4096)
                if not chunk:
                    break
                response += chunk

            print("Received response from target server.")

        # Send the HTTP response back to the client
        server_socket.sendto(response, client_address)
        print("Response forwarded to client.")
    except Exception as e:
        print("Error:", e)

def start_relay_server():
    # Create a socket for the relay server
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((RELAY_HOST, RELAY_PORT))
        print(f"Relay server running on {RELAY_HOST}:{RELAY_PORT}...")

        while True:
            # Receive data from the client
            data, client_address = server_socket.recvfrom(4096)
            print(f"Connection established with {client_address}")
            handle_client(data, client_address, server_socket)

if __name__ == "__main__":
    start_relay_server()