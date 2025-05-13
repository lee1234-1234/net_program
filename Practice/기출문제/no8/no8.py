import socket

# Relay server configuration
RELAY_HOST = 'localhost'
RELAY_PORT = 9000

# Target server configuration
TARGET_HOST = 'www.daum.net'
TARGET_PORT = 80

def handle_client(client_socket):
    try:
        # Receive HTTP request from the browser
        request = client_socket.recv(4096).decode('utf-8')
        print("Received request from browser:")
        print(request)

        # Extract the request line (first line of the HTTP request)
        request_line = request.split('\r\n')[0]
        print("Request line:", request_line)

        # Create a new socket to connect to the target server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as target_socket:
            target_socket.connect((TARGET_HOST, TARGET_PORT))

            # Construct a minimal HTTP request to the target server
            target_request = f"{request_line}\r\nHost: {TARGET_HOST}\r\n\r\n"
            print("Forwarding request to target server:")
            print(target_request)

            # Send the HTTP request to the target server
            target_socket.sendall(target_request.encode('utf-8'))

            # Receive the HTTP response from the target server
            response = b""
            while True:
                chunk = target_socket.recv(4096)
                if not chunk:
                    break
                response += chunk

            print("Received response from target server.")
        
        # Send the HTTP response back to the browser
        client_socket.sendall(response)
        print("Response forwarded to browser.")
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

def start_relay_server():
    # Create a socket for the relay server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((RELAY_HOST, RELAY_PORT))
        server_socket.listen(5)
        print(f"Relay server running on {RELAY_HOST}:{RELAY_PORT}...")

        while True:
            # Accept a connection from the browser
            client_socket, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            handle_client(client_socket)

if __name__ == "__main__":
    start_relay_server()