from socket import *

# Create a server socket bound to port 9999
server = create_server(('', 9999))

# Accept a connection from a client
conn, addr = server.accept()

# Send a message to the connected client
conn.send(b'This is IoT world!!!')

# Close the connection
conn.close()