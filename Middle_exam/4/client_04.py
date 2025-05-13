import socket
import struct

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        request = input("Enter '1', '2', '3': ").strip()
        if request not in ['1', '2', '3']:
            print("Enter '1', '2', '3': ")
            continue
        client_socket.sendto(request.encode(), (SERVER_ADDRESS, SERVER_PORT))
        response, _ = client_socket.recvfrom(6)
        temperature, humidity, light = struct.unpack('!hhh', response)
        print(f"Temp= {temperature}, Humid= {humidity}, Lumi= {light}")

except KeyboardInterrupt:
    print("\nClient terminated.")
finally:
    client_socket.close()
    
    
    