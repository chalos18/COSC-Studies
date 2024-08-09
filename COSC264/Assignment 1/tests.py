"""
Suppose you have your server program as server.py and your client program as client.py
and you want to run your server program at port 1234

Open two linux terminals

In one terminal you start the server by using the command:
python3 server.py 1234

In the other terminal you start the client by using the command:
python3 client.py localhost 1234
"""

# Tests your client with the command:
#     python3 client.py time localhost 5878
# A server is listening on port 5878 and
# will send an English time response with the
# specific date and time:
#     17/3/2019 05:06
# Similar to running the server with the command:
#     python3 server.py 5878 30617 21233

# Result
"""
Time request sent to 127.0.0.1:5878
English response received:
Text: The current time is 05:06
Date: 17/3/2019
Time: 05:06

--------------------------------------------------
Server log:
    Received:
      36fb 0001 0002
    Sent:
      36fb 0002 0001 07e3 0311 0506 1954 6865
      2063 7572 7265 6e74 2074 696d 6520 6973
      2030 353a 3036

Sockets still open: None
Explicitly bound ports: None
Socket timeouts: [1.0]
"""

# Tests your client with the command:
#     python3 client.py date localhost 13581
# A server is listening on port 13581 and
# will send a German date response with the
# specific date and time:
#     2/5/2012 02:23
# Similar to running the server with the command:
#     python3 server.py 5878 21233 13581

"""
Date request sent to 127.0.0.1:13581
German response received:
Text: Heute ist der 2. Mai 2012
Date: 2/5/2012
Time: 02:23

--------------------------------------------------
Server log:
    Received:
      36fb 0001 0001
    Sent:
      36fb 0002 0003 07dc 0502 0217 1948 6575
      7465 2069 7374 2064 6572 2032 2e20 4d61
      6920 3230 3132

Sockets still open: None
Explicitly bound ports: None
Socket timeouts: [1.0]
"""

# Tests your client with the command:
#     python3 client.py date localhost 13581
# A server is listening on port 13581 and
# will send a Māori date response with the
# specific date and time:
#     12/4/2020 08:57
# Similar to running the server with the command:
#     python3 server.py 30617 13581 5878

"""
Date request sent to 127.0.0.1:13581
Māori response received:
Text: Ko te rā o tēnei rā ko Paenga-whāwhā 12, 2020
Date: 12/4/2020
Time: 08:57

--------------------------------------------------
Server log:
    Received:
      36fb 0001 0001
    Sent:
      36fb 0002 0002 07e4 040c 0839 324b 6f20
      7465 2072 c481 206f 2074 c493 6e65 6920
      72c4 8120 6b6f 2050 6165 6e67 612d 7768
      c481 7768 c481 2031 322c 2032 3032 30

Sockets still open: None
Explicitly bound ports: None
Socket timeouts: [1.0]
"""
