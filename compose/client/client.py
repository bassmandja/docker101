import socket
import sys

HOST, PORT = "localhost", 1234
data = " ".join(sys.argv[1:])
spacing = '    '
print(f'{spacing} client: starting up')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print(f'{spacing} client: connecting to {HOST}:{PORT}')
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")

print(f'{spacing} client sent:     {data}')
print(f'{spacing} client received: {received}')
