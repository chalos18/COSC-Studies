"""
Suppose you have your server program as server.py and your client program as client.py
and you want to run your server program at port 1234

Open two linux terminals

In one terminal you start the server by using the command:
python3 server.py 1234

In the other terminal you start the client by using the command:
python3 client.py localhost 1234

Your program should only output the first part of the 'Result' column. The blank line, the dashed line, and everything below them will be produced automatically by our tests.
Your client will be tested against a sample server, so it is vital that you have followed the protocol exactly as it is specified. 
This sample server will send back dates/times that differ from the current date/time.
Checking might take a few seconds to process; please be patient.
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


# Server Tests

# Tests your server by running the command:
#     python3 server.py 30617 5878 21233
# A client will be run using the following command
# to send an English request to your server:
#     python3 client.py date localhost 30617
# In CodeRunner your server will be given the
# following date and time by the datetime module:
#     7/7/2024 09:41

"""
Binding English to port 30617
Binding Māori to port 5878
Binding German to port 21233
Waiting for requests...
English received date request from 127.0.0.1
Response sent
Waiting for requests...

--------------------------------------------------
Client log:
    Sent to port 30617:
      36fb 0001 0001
    Received from port 30617:
      36fb 0002 0001 07e8 0707 0929 1c54 6f64
      6179 2773 2064 6174 6520 6973 204a 756c
      7920 372c 2032 3032 34

Sockets still open: None
Explicitly bound ports: [30617, 5878, 21233]
Select timeouts: [None, None]
"""

# Tests your server by running the command:
#     python3 server.py 13581 5878 21233
# A client will be run using the following command
# to send a German request to your server:
#     python3 client.py time localhost 21233
# In CodeRunner your server will be given the
# following date and time by the datetime module:
#     24/12/2012 08:02
"""
Binding English to port 13581
Binding Māori to port 5878
Binding German to port 21233
Waiting for requests...
German received time request from 127.0.0.1
Response sent
Waiting for requests...

--------------------------------------------------
Client log:
    Sent to port 21233:
      36fb 0001 0002
    Received from port 21233:
      36fb 0002 0003 07dc 0c18 0802 1544 6965
      2055 6872 7a65 6974 2069 7374 2030 383a
      3032

Sockets still open: None
Explicitly bound ports: [13581, 5878, 21233]
Select timeouts: [None, None]
"""

# Tests your server by running the command:
#     python3 server.py 21233 13581 30617
# A client will be run using the following command
# to send a Māori request to your server:
#     python3 client.py date localhost 13581
# In CodeRunner your server will be given the
# following date and time by the datetime module:
#     2/1/2012 12:10
"""
Binding English to port 21233
Binding Māori to port 13581
Binding German to port 30617
Waiting for requests...
Māori received date request from 127.0.0.1
Response sent
Waiting for requests...

--------------------------------------------------
Client log:
    Sent to port 13581:
      36fb 0001 0001
    Received from port 13581:
      36fb 0002 0002 07dc 0102 0c0a 2d4b 6f20
      7465 2072 c481 206f 2074 c493 6e65 6920
      72c4 8120 6b6f 204b 6f68 692d 74c4 8174
      6561 2032 2c20 3230 3132

Sockets still open: None
Explicitly bound ports: [21233, 13581, 30617]
Select timeouts: [None, None]
"""