import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # creates a socket object
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    # connect to server and send message
    data = s.recv(1024) # read server's reply

print(f"Received {data!r}")


# Unlike send(), sendall() continues to send data from bytes until either all data has been sent or an error occurs.
# None is returned on success.
# (Therefore, we don't have to manually check if the entire data is sent)

