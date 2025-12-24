import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET means use IPv4 (Address family)
    # SOCK_STREAM means use TCP (Socket type)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() # returns a socket object
    # different from the socket returned by listen()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # a blocking call (temporarily stops the execution of code)
            data = conn.recv(1024)
            if not data:
                # if an empty byte object is returned, signals the client closed the connection
                break
            conn.sendall(data)
            
# ------
# by using 'with context manager', we no longer have to worry about closing the socket

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

# server must bind, listen, accept
# client must connect
# they both can send and receive
# three-way handshake must be established

# at the end both server and client close their respective connections.

