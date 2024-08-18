import socket
import sys

# constants
MAGIC_NO = 0x36FB
PACKET_TYPE = 0x0001

RESPONSE_PACKET_TYPE = 0x0002

LANGUAGES = [0x0001, 0x0002, 0x0003]

VALID_REQUEST_TYPES = ["date", "time"]


# helper functions or classes
def print_response(response):
    language_code = (response[4] << 8) | response[5]
    text_start_index = 13
    text_length = response[12]
    text_end_index = text_start_index + text_length
    text = response[text_start_index:text_end_index].decode("utf-8")

    languages = {0x0001: "English", 0x0002: "Māori", 0x0003: "German"}
    language = languages.get(language_code, "Unknown")

    day = response[9]
    month = response[8]
    year = (response[6] << 8) | response[7]
    hour = response[10]
    minute = response[11]

    # might need to change the hour and minute to have a leading 0
    print(f"{language} response received:")
    print(f"Text: {text}")
    print(f"Date: {day}/{month}/{year}")
    print(f"Time: {hour:02d}:{minute:02d}")


def text_validation(response):
    # Length
    text_length = response[12]
    if len(response) != 13 + text_length:
        print("ERROR: Packet text length is incorrect")
        sys.exit(1)  # Exit the application

    # Text
    text_end_index = 13 + text_length
    if text_end_index > len(response):
        print("ERROR: Packet text length is incorrect")
        sys.exit(1)  # Exit the application

    # UTF-8 string
    try:
        text = response[13:text_end_index].decode("utf-8")
    except UnicodeDecodeError:
        print("ERROR: Packet has invalid text")
        sys.exit(1)  # Exit the application


def date_time_validation(response):
    # Year
    year = (response[6] << 8) | response[7]
    if not (0 <= year < 2100):
        print("ERROR: Packet has invalid year")
        sys.exit(1)  # Exit the application

    # Month
    month = response[8]
    if not (1 <= month <= 12):
        print("ERROR: Packet has invalid month")
        sys.exit(1)  # Exit the application

    # Day
    day = response[9]
    if not (1 <= day <= 31):
        print("ERROR: Packet has invalid day")
        sys.exit(1)  # Exit the application

    # Hour
    hour = response[10]
    if not (0 <= hour <= 23):
        print("ERROR: Packet has invalid hour")
        sys.exit(1)  # Exit the application

    # Minute
    minute = response[11]
    if not (0 <= minute <= 59):
        print("ERROR: Packet has invalid minute")
        sys.exit(1)  # Exit the application


def validation_checks(response):
    if len(response) < 13:
        print("ERROR: Packet is too small to be a DT_Response")
        sys.exit(1)  # Exit the application  # discard the packet

    # MagicNo
    magic_no = (response[0] << 8) | response[1]
    if magic_no != MAGIC_NO:
        print("ERROR: Packet magic number is incorrect")
        sys.exit(1)  # Exit the application

    # PacketType
    packet_type = (response[2] << 8) | response[3]
    if packet_type != 0x0002:
        print("ERROR: Packet is not a DT_Response")
        sys.exit(1)  # Exit the application

    # LanguageCode
    language_code = (response[4] << 8) | response[5]
    if language_code not in LANGUAGES:
        print("ERROR: Packet has invalid language")
        sys.exit(1)  # Exit the application

    # validates the date/time fields
    date_time_validation(response)

    # validates the text fields
    text_validation(response)

    print_response(response)


def create_dt_request(request_type):
    # Requests either the date or the current time of day from the server
    # 3 fields * 2 bytes each = 6 bytes
    dt_request = bytearray(6)

    # 16-bit field MagicNo checks whether a packet actually belongs to our DateTime protocol
    dt_request[0] = (MAGIC_NO >> 8) & 0xFF
    dt_request[1] = MAGIC_NO & 0xFF

    # 16-bit field PacketType indicates the packet type within our DateTime protocol
    dt_request[2] = (0x0001 >> 8) & 0xFF
    dt_request[3] = 0x0001 & 0xFF

    # 16-bit field RequestType 16-bit field RequestType indicates the particular type of request the client makes
    if request_type == "date":
        REQUEST_TYPE = 0x0001
    elif request_type == "time":
        REQUEST_TYPE = 0x0002

    dt_request[4] = (REQUEST_TYPE >> 8) & 0xFF
    dt_request[5] = REQUEST_TYPE & 0xFF

    return dt_request


def resolve_hostname(hostname):
    try:
        addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET)
        for info in addr_info:
            return info[4][0]
    except socket.gaierror:
        print("ERROR: Hostname resolution failed")
        sys.exit(1)

def validate_port(port_str):
    try:
        port = int(port_str)
        # Check if positive integer
        if port <= 0:
            print(f"ERROR: Given port '{port_str}' is not a positive integer")
            sys.exit(1)
        return port
    except ValueError:
        # If conversion to int fails
        print(f"ERROR: Given port '{port_str}' is not a positive integer")
        sys.exit(1)

# UDP Client
"""
The client creates a socket and attempts to make a connection to the server. 
The client has to know the server's URL and the port at which the service exists
"""
def main():
    s = None
    try:
        # There should be exactly three command line arguments
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of command line arguments")
            sys.exit(1)

        request_type = sys.argv[1]
        if request_type not in VALID_REQUEST_TYPES:
            print(f"ERROR: Request type '{request_type}' is not valid")
            sys.exit(1)

        hostname = sys.argv[2]
        host_ip = resolve_hostname(hostname)

        # host --> IP address
        port_str = sys.argv[3]
        port = validate_port(port_str)

        # All three ports must be between 1,024 and 64,000 (inclusive)
        if not (1024 <= port <= 64000):
            print(f"ERROR: Given port '{port}' is not in the range [1024, 64000]")
            sys.exit(1)

        # Create a UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)

    except socket.error:
        print("ERROR: Socket creation failed")
        sys.exit(1)

    # Prepare to send and receive data
    try:
        dt_request = create_dt_request(request_type)
        # Send the request to the UDP server
        try:
            s.sendto(dt_request, (host_ip, port))
            print(f"{request_type.capitalize()} request sent to {host_ip}:{port}")
        # except socket.error:
        except:
            print("ERROR: Sending failed")
            sys.exit(1)

        # Receive a response from the server and validate it
        try:
            response, _ = s.recvfrom(4096)
            validation_checks(response)
        except socket.timeout:
            print("ERROR: Receiving timed out")
            sys.exit(1)
        except socket.error:
            print("ERROR: Receiving failed")
            sys.exit(1)

    finally:
        if s:
            s.close()


main()
