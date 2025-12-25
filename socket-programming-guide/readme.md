#### What are privileged and non-privileged ports?
On transport protocols (tcp, udp, sctp ...), ports 1-1023 are by default privileged.
A process needs root permissions to bind to one of these ports.


- Python' socket API maps directly to system calls and their C counterparts.
It provides classes that make using low-level socket functions easier.

- Applications use the loopback interface (localhost or 127.0.0.1) to communicate with other processes running on host and for security and isolation from external network.

#### Another problem:
- How to handle multiple connections concurrently?
- We need to call send() and recv() until all data is sent or received.
There are few ways to handle concurrency. One is to use asyncio (added to standard library in python 3.4)<br>
Another more traditional choice is to use threads.

if your application needs to scale, using concurrency is a necessity.

here we'll use select().
we also use selectors module (standard library) for high level multiplexing.<br>
selectors module is built upon the select module primitive.<br>

asyncio uses single-threaded cooperative multitasking and an event loop to manage tasks.<br>
with select(), we'll be writing our own version of event loop.<br>
Network applications are I/O bound.<br>

We'll create a server and client that handle multiple connections, using selector object created from selectors module.<br>

(Discontinued for now..., too advanced)