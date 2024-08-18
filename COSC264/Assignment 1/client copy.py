"""
A client sends a DT Request packet to the server. The client is started on the same host or different host and takes
three paramaters as command line arguments. If any of the following conditions are not met, the server should print
the corresponding error message and exit immdediately.

1. If there are not exactly three command line arguments, the client should print "ERROR: Incorrect number of command line arguments" and exit.
2. The first parameter must be either the string “date” or the string “time”, letting the user specify what they wish to see. If it is not equal to either of these, 
the client program should print a message of the form "ERROR: Request type '{x}' is not valid" where {x} is the invalid argument and then exit.
3. The second parameter is either an IP address in dotted-decimal notation (e.g. “130.66.22.212”) or the hostname of the computer running the server (e.g. “datetime.mydomain.nz”). 
The client must attempt to convert this to an IP address using the getaddrinfo() function. If this conversion fails (e.g. because the hostname does not exist or 
an IP address given in dotted-decimal notation is not well-formed), then the client should print "ERROR: Hostname resolution failed" and then exit.
4. The third parameter is the port number to use on the server.
5. The port number must be a positive integer. If not, it should print a message of the form "ERROR: Given port '{x}' is not a positive integer" where {x} is the invalid port argument that was given.
6. The port number must be between 1,024 and 64,000 (inclusive). If not, it should print a message of the form "ERROR: Given port '{x}' is not in the range [1024, 64000]" 
where {x} is the invalid port argument that was given.

- Call main() from the global level to launch the program.
- Contain no more than 15 global constants.
- Contain functions that are each no more than 30 statements long.
- Use bit-fiddling and bytearrays to construct your packets. Use of modules like struct is banned.
"""

import socket
from socket import AF_INET, SOCK_DGRAM, htonl, htons, ntohl, ntohs, getaddrinfo

# constants
socket.AF_INET
socket.SOCK_DGRAM

# helper functions or classes

def validation_checks(response):
    if len(response) != 13 bytes of data:
        print("ERROR: Packet is too small to be a DT_Response")
        # discard the packet
    
    # MagicNo
    if response[0] != 0x36FB:
        print("ERROR: Packet magic number is incorrect")

    # PacketType
    if response[1] != 0x0002:
        print("ERROR: Packet is not a DT_Response")

    # LanguageCode
    languages = [0x0001, 0x0002, 0x0003]
    if response[2] not in languages:
        print("ERROR: Packet has invalid language")
    # Year
    if response[3] != 2100:
        print("ERROR: Packet has invalid year")

    # Month
    months = [_ for _ in range (1, 13)]
    if response[4] not in months:
        print("ERROR: Packet has invalid month")

    # Day
    days = [_ for _ in range (1, 32)]
    if response[5] not in days:
        print("ERROR: Packet has invalid day")

    # Hour
    hours = [_ for _ in range (0, 24)]
    if response[6] not in hours:
        print("ERROR: Packet has invalid hour")

    # Minute
    minutes = [_ for _ in range (0, 60)]
    if response[7] not in minutes:
        print("ERROR: Packet has invalid minute")

    # Length
    if len(response) != the sum of 13(for the fixed header) + contents of length field:
        print("ERROR: Packet text length is incorrect")
    
    # Text
    if response[9] cannot be decoded as a UTF-8 string:
        print("ERROR: Packet has invalid text")


# UDP Client
"""
The client creates a socket and attempts to make a connection to the server. 
The client has to know the server's URL and the port at which the service exists
"""
def main():
    host = '127.0.0.1'
    port = 12345

    # Get address info from server
    services = socket.getaddrinfo(host, port, family=0, type=socket.SOCK_DGRAM, proto=0, flags=0)
    
    # Create a UDP socket
    s = socket(family=AF_INET, type=SOCK_DGRAM)

    # with UDP connect is not required, its more common to use sendto and recvfrom directly
    server_address = (host, port)
    s.connect(server_address)

    # Prepare to send and receive data
    try:
        # Requests either the date or the current time of day from the server
        dt_request = bytearray(32)

        #16-bit field MagicNo checks whether a packet actually belongs to our DateTime protocol
        dt_request[0] = 0x36FB
        # 16-bit field PacketType indicates the packet type within our DateTime protocol
        dt_request[1] = 0x0001
        # 16-bit field RequestType 16-bit field RequestType indicates the particular type of request the client makes
        if client requests current date:
            dt_request[2] = 0x0001
        else if client requests the current time of day:
            dt_request[2] = 0x0002
    
        # send the message to the UDP server
        amount = s.send(dt_request)

        # Receive a response from the server (optional for UDP)
        response, server = s.recvfrom(4096)
        print('Received: ', response.decode())

        # Upon receiveing the packet, the client must check:
        validation_checks(response)
    
    finally:
        s.close()

main()
