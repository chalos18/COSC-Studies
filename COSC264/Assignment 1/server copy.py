"""
A client sends a DT Request packet to the server. The server then checks:

1. Whether the packet contains exactly six bytes of data. If not, it should print "ERROR: Packet length incorrect for a DT_Request, dropping packet"
2. Whether the MagicNo field contains the value 0x36FB. If not, it should print "ERROR: Packet magic number is incorrect, dropping packet"
3. Whether the PacketType field contains the value 0x0001. If not, it should print "ERROR: Packet is not a DT_Request, dropping packet"
4. Whether the RequestType field contains either the value 0x0001 or 0x0002. If not, it should print "ERROR: Packet has invalid type, dropping packet"

If all conditions are met then the server acceps the packet for further processing. If not met,
the server will print the appropriate error message and discard the packet.

- Call main() from the global level to launch the program.
- Contain no more than 15 global constants.
- Contain functions that are each no more than 30 statements long.
- Use bit-fiddling and bytearrays to construct your packets. Use of modules like struct is banned.
- Use the datetime module to get the correct dates/times. Please do not use any other means of getting the date or time, 
as the date/times your program will be tested with are not necessarily the current date/time. 
- Clarification 8 August: Your server should only be making one datetime call per client request.
"""
import datetime
from socket import AF_INET, SOCK_DGRAM, socket, htonl, htons, ntohl, ntohs, getaddrinfo

# constants
socket.AF_INET
socket.SOCK_DGRAM

# helper functions or classes

# these functions convert from host (h) to network(n) representation and vice versa
netlong = htonl(hostlong)
netshort = htons(hostshort)
hostlong = ntohl(netlong)
hostshort = ntohs(netshort)

# UDP Server - no listen and accept calls necessary
def main():
    # link(bind) the socket to address
    # There should be exactly three command line arguments
    if not english_port or not te_reo_maori_port or not german_port:
        print("ERROR: Incorrect number of command line arguments")

    # All three port numbers must be different
    if english_port == te_reo_maori_port or german_port:
        print("ERROR: Duplicate ports given")
    if te_reo_maori_port == english_port or german_port:
        print("ERROR: Duplicate ports given")
    if german_port == te_reo_maori_port or english_port:
        print("ERROR: Duplicate ports given")

    ports = [english_port, te_reo_maori_port, german_port]
    for port in ports:
        # All three port numbers must be positive integers
        if port < 0:
            print(f"ERROR: Given port '{port}' is not a positive integer")
        # All three ports must be between 1,024 and 64,000 (inclusive)
        if 1024 > port < 64000:
            print(f"ERROR: Given port '{port}' is not in the range [1024, 64000]")

    host = "localhost:8080"

    # Create a socket for UDP
    try:
        s_english = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_maori = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_german = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print("ERROR: Socket creation failed")
        s_english.close()
        s_maori.close()
        s_german.close()

    try:
        print(f"Binding English to port {number}")
        s_english.bind((host, english_port))

        print(f"Binding Māori to port {number}")
        s_maori.bind((host, te_reo_maori_port))

        print(f"Binding German to port {number}")
        s_german.bind((host, german_port))

    except:
        print("ERROR: Socket binding failed")
        s_english.close()
        s_maori.close()
        s_german.close()

    print("Waiting for requests...")

    try:
        while True:
            # Receive a message from the client
            data, address = s.recvfrom(4096)
            print(f"Received {data.hex()} from {address}")

            client_data_validation_check(data)

            # Prepare a response
            response = create_dt_response()

            # Send the response back to the client
            s.sendto(response, address)
    finally:
        s.close()


main()
