#### What are privileged and non-privileged ports?
On transport protocols (tcp, udp, sctp ...), ports 1-1023 are by default privileged.
A process needs root permissions to bind to one of these ports.


Python' socket API maps directly to system calls and their C counterparts.
It provides classes that make using low-level socket functions easier.