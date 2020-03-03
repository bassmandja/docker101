import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
spacing = '    '
print(f'{spacing} client: starting up')
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print(f'{spacing} client sent:     {data}')
print(f'{spacing} client received: {received}')
