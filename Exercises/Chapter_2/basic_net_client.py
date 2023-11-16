import socket

HOST = 'localhost'
PORT = 50007              # The same port as used by the server
print("About to connect...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello, world'.encode("UTF"))
    print("Message sent.")