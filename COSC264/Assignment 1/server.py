from datetime import datetime
import select
import sys
import socket

# constants
MAGIC_NO = 0x36FB

RESPONSE_PACKET_TYPE = 0x0002

VALID_REQUEST_TYPES = {0x0001, 0x0002}

ENGLISH = 0x0001
TE_REO_MAORI = 0x0002
GERMAN = 0x0003
LANGUAGE_CODES = {ENGLISH: "English", TE_REO_MAORI: "Māori", GERMAN: "German"}


# helper functions or classes
MONTH_NAMES = {
    "English": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
    "Te Reo Māori": [
        "Kohi-tātea",
        "Hui-tanguru",
        "Poutū-te-rangi",
        "Paenga-whāwhā",
        "Haratua",
        "Pipiri",
        "Hōngingoi",
        "Here-turi-kōkā",
        "Mahuru",
        "Whiringa-ā-nuku",
        "Whiringa-ā-rangi",
        "Hakihea",
    ],
    "German": [
        "Januar",
        "Februar",
        "März",
        "April",
        "Mai",
        "Juni",
        "Juli",
        "August",
        "September",
        "Oktober",
        "November",
        "Dezember",
    ],
}


def get_month(month, language):
    return MONTH_NAMES[language][month - 1]


def textual_representation_generation(
    language_code, request_type, year, month, day, hour, minute
):
    hour_str = f"{hour:02d}"
    minute_str = f"{minute:02d}"

    if language_code == ENGLISH:
        if request_type == "date":
            return f"Today's date is {get_month(month, 'English')} {day}, {year}"
        elif request_type == "time":
            return f"The current time is {hour_str}:{minute_str}"
    elif language_code == TE_REO_MAORI:
        if request_type == "date":
            return f"Ko te rā o tēnei rā ko {get_month(month, 'Te Reo Māori')} {day}, {year}"
        elif request_type == "time":
            return f"Ko te wā o tēnei wā {hour_str}:{minute_str}"
    elif language_code == GERMAN:
        if request_type == "date":
            return f"Heute ist der {day}. {get_month(month, 'German')} {year}"
        elif request_type == "time":
            return f"Die Uhrzeit ist {hour_str}:{minute_str}"


def client_data_validation_check(data):
    # Upon receiving a packet, the server must check:
    if len(data) != 6:
        print("ERROR: Packet length incorrect for a DT_Request, dropping packet")
        return None

    magic_no = (data[0] << 8) | data[1]
    if magic_no != MAGIC_NO:
        print("ERROR: Packet magic number is incorrect, dropping packet")
        return None

    packet_type = (data[2] << 8) | data[3]
    if packet_type != 0x0001:
        print("ERROR: Packet is not a DT_Request, dropping packet")
        return None

    request_type = (data[4] << 8) | data[5]
    if request_type not in VALID_REQUEST_TYPES:
        print("ERROR: Packet has invalid type, dropping packet")
        return None

    return "date" if request_type == 0x0001 else "time"


def create_dt_response(language_code, request_type):
    """
    Prepares a DT-Response packet
    """

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    text = textual_representation_generation(
        language_code, request_type, year, month, day, hour, minute
    )

    text_bytes = text.encode("utf-8")
    text_length = len(text_bytes)
    if text_length > 255:
        print("ERROR: Text too long, dropping packet")
        return None

    # prepare a response message resp if all conditions are met
    # returns both the date and current time of day in a binary representation,
    # followed by either the date or the time of day (depending on the client's choice) in a textual representation
    dt_response = bytearray(13 + text_length)

    # 16-bit field MagicNo checks whether a packet actually belongs to our DateTime protocol
    dt_response[0] = (MAGIC_NO >> 8) & 0xFF
    dt_response[1] = MAGIC_NO & 0xFF

    # 16-bit field PacketType indicates the packet type within our DateTime protocol
    dt_response[2] = (RESPONSE_PACKET_TYPE >> 8) & 0xFF
    dt_response[3] = RESPONSE_PACKET_TYPE & 0xFF

    # LanguageCode indicates the language used for textual representation
    dt_response[4] = (language_code >> 8) & 0xFF
    dt_response[5] = language_code & 0xFF

    # 16-bit field Year contains the value for the year as a non-negative integer
    dt_response[6] = (year >> 8) & 0xFF
    dt_response[7] = year & 0xFF
    # 8-bit field Month contains the value for the month as a non-negative integer
    dt_response[8] = month
    # 8-bit field Day contains the value for the day of the month as a non-negative integer
    dt_response[9] = day
    # 8-bit field Hour contains the hour of the day in 24-hour format. This number is allowed to range from 0 to 23
    dt_response[10] = hour
    # 8-bit field Minute contains the minute within the hour. This number is allowed to range from 0 to 59
    dt_response[11] = minute
    # 8-bit field Length indicates the length of the textual representation in bytes

    dt_response[12] = text_length
    # print(f"Text Length: {text_length}")
    # Text field
    dt_response[13:] = text_bytes

    # dt_response_hex = dt_response.hex()
    # print(f"Response packet (hex): {dt_response_hex}")
    # packet_bytes = bytes.fromhex(dt_response_hex)
    # print(packet_bytes)

    return dt_response


def socket_creation():
    try:
        s_english = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_maori = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_german = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print(f"ERROR: Socket creation failed")
        sys.exit(1)

    return s_english, s_maori, s_german


def socket_binding(ports, s_english, s_maori, s_german):
    host = "localhost"

    try:
        print(f"Binding English to port {ports[0]}")
        s_english.bind((host, ports[0]))

        print(f"Binding Māori to port {ports[1]}")
        s_maori.bind((host, ports[1]))

        print(f"Binding German to port {ports[2]}")
        s_german.bind((host, ports[2]))

    except socket.error:
        print(f"ERROR: Socket binding failed")
        # Close sockets if they were created before the error
        for socket in (s_english, s_maori, s_german):
            if socket:
                socket.close()
        sys.exit(1)


def socket_creation(ports, s_english, s_maori, s_german):
    # Define the ports and language labels
    ports = [s_english, s_maori, s_german]  # Example port numbers, adjust as needed
    languages = ["English", "Māori", "German"]

    # Create a list to hold socket references
    sockets = []

    # Iterate over ports and languages to create and bind sockets
    for i in range(3):
        language = languages[i]
        port = ports[i]

        # Print status message before socket creation and binding
        print(f"Binding {language} to port {port}")

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sockets.append(s)
        except socket.error:
            print("ERROR: Socket creation failed")
            for sock in sockets:
                sock.close()
            sys.exit(1)

        try:
            # Bind the socket
            s.bind(("localhost", port))
        except socket.error:
            print("ERROR: Socket binding failed")
            for sock in sockets:
                sock.close()
            sys.exit(1)

    return sockets

# def receiving_data(s):
#     try:
#         data, address = s.recvfrom(4096)
#     except socket.timeout:
#         print("ERROR: Receiving timed out, dropping packet")
#         return None
#     except socket.error:
#         print(f"ERROR: Receiving failed, dropping packet")
#         return None
#     return data,address

def socket_validation(sockets, readable):
    for s in readable:
        try:
            data, address = s.recvfrom(4096)
        except socket.timeout:
            print("ERROR: Receiving timed out, dropping packet")
            print("Waiting for requests...")
            return
        except socket.error:
            print(f"ERROR: Receiving failed, dropping packet")
            print("Waiting for requests...")
            return

        request_type = client_data_validation_check(data)
        if request_type is None:
            print("Waiting for requests...")
            continue

        print(
            f"{LANGUAGE_CODES[sockets[s]]} received {request_type} request from {address[0]}"
        )

        response = create_dt_response(sockets[s], request_type)
        try:
            if response:
                s.sendto(response, address)
                print("Response sent")
        except socket.error:
            print("ERROR: Sending failed, dropping packet")

        print("Waiting for requests...")


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


# UDP Server
def main():
    s_english = s_maori = s_german = None
    try:
        # There should be exactly three command line arguments
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of command line arguments")
            sys.exit(1)

        # All three port numbers must be positive integers
        english_port = validate_port(sys.argv[1])
        te_reo_maori_port = validate_port(sys.argv[2])
        german_port = validate_port(sys.argv[3])

        # All three port numbers must be different
        ports = [english_port, te_reo_maori_port, german_port]
        if len(set(ports)) < 3:
            print("ERROR: Duplicate ports given")
            sys.exit(1)

        # All three ports must be between 1,024 and 64,000 (inclusive)
        for port in ports:
            if not (1024 <= port <= 64000):
                print(f"ERROR: Given port '{port}' is not in the range [1024, 64000]")
                sys.exit(1)

        # Create sockets for UDP
        socket_list = socket_creation(
            ports, english_port, te_reo_maori_port, german_port
        )

        s_english = socket_list[0]
        s_maori = socket_list[1]
        s_german = socket_list[2]

        print("Waiting for requests...")

        sockets = {s_english: ENGLISH, s_maori: TE_REO_MAORI, s_german: GERMAN}

        while True:
            try:
                readable, _, _ = select.select(list(sockets.keys()), [], [])

                socket_validation(sockets, readable)

            except socket.error as e:
                print(f"ERROR: {e}")

    finally:
        # Make sure sockets are fully closed
        for socket in (s_english, s_maori, s_german):
            if socket:
                socket.close()
        sys.exit(0)


main()
