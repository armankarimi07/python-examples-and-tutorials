import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            
# ------
# by using 'with context manager', we no longer have to worry about closing the socket

# args provided to socket(): address family and socket type
# the constant AF_INET -> IPv4
# SOCK_STREAM -> indicates TCP

# bind() -> to associate the socket with a network interface and port number

# (HOST, PORT) this tuple is known as address family

# by using localhost, only processes on the host will be able to connect to the server

# listen() -> enables a server to accept new connections, making it a listening port
# listen() takes a backlog -> number of unaccepted connections before refusing new ones
# if not provided, default will be used (system dependent)

# listen() blocks execution, waiting for incoming connection, if a client connects...
# a new socket object is returned representing a tuple, holding address of client
# the new socket is distinct from the listening scoket

# blocking calls -> temporarily stop the execution of code until they are done

