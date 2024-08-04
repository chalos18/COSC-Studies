def checksum(header):
    """Takes a single bytearray parameter (representing an IPv4 header)
    and returns the header checksum.
    """
    if len(header) < 20:
        raise ValueError("Header is too short")
    if len(header) % 4 != 0:
        raise ValueError("Header does not contain a multiple of 4 bytes")

    # print(header)
    n = len(header) // 2

    x = 0

    # Start at the first byte, go all the way to the last byte
    # Move two bytes forward at a time
    for i in range(0, len(header), 2):
        # Extract 16-bit integer from the header
        # Big-endian: higher byte first
        byte1 = header[i]  # First byte of the 16-bit number
        byte2 = header[i + 1]  # Second byte of the 16-bit number
        # Combine the two bytes into a 16-bit integer
        bit_value = (byte1 << 8) | byte2  # Shift the first byte to the left and combine
        x += bit_value

    while x > 0xFFFF:
        lowest16 = x & 0xFFFF
        carry = x >> 16
        x = lowest16 + carry

    checksum = ~x & 0xFFFF

    return checksum


# A valid header should evaluate to 0.
header1 = bytearray(
    [
        0x45,
        0x0,
        0x0,
        0x1E,
        0x4,
        0xD2,
        0x0,
        0x0,
        0x40,
        0x6,
        0x20,
        0xB4,
        0x12,
        0x34,
        0x56,
        0x78,
        0x98,
        0x76,
        0x54,
        0x32,
    ]
)
# print(checksum(header1))


# A header whose checksum has not been set yet (The result of the
# function call is the value the checksum field should be set to.)
# Result should be 8372
empty_checksum_header = bytearray(
    [
        0x45,
        0x0,
        0x0,
        0x1E,
        0x4,
        0xD2,
        0x0,
        0x0,
        0x40,
        0x6,
        0x0,
        0x0,
        0x12,
        0x34,
        0x56,
        0x78,
        0x98,
        0x76,
        0x54,
        0x32,
    ]
)
# print(checksum(empty_checksum_header))

# Don't forget to include the definition for the checksum function that you
# wrote for the previous question here!


def basic_packet_check(packet):
    """Performs basic correctness checks on an IPv4 packet.
    Returns True if all checks pass.
    Raises ValueError with a specific message if any check fails.
    """
    if len(packet) < 20:
        raise ValueError("Packet does not contain a full IP header")

    # first 4 bits of the first byte
    version = packet[0] >> 4
    if version != 4:
        raise ValueError("Packet version number must equal 4")

    # last 4 bits of the first byte
    hdr_len = packet[0] & 0x0F
    if hdr_len < 5:
        raise ValueError("Packet hdrlen field must be at least 5")

    # Note that the header length field
    # gives the length of the IPv4 header in multiples of 32 bits (4 bytes)
    header_length = hdr_len * 4
    if len(packet) < header_length:
        raise ValueError("Packet length is less than the specified header length")

    header = packet[:header_length]
    if checksum(header) != 0:
        raise ValueError("Packet checksum failed")

    # (bytes 2 and 3)
    total_length = (packet[2] << 8) | packet[3]
    if total_length != len(packet):
        raise ValueError(
            "Packet totallength field is inconsistent with the packet length"
        )

    return True


pkt1 = bytearray(
    [
        0x45,
        0x0,
        0x0,
        0x1E,
        0x4,
        0xD2,
        0x0,
        0x0,
        0x40,
        0x6,
        0x20,
        0xB4,
        0x12,
        0x34,
        0x56,
        0x78,
        0x98,
        0x76,
        0x54,
        0x32,
        0x0,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
    ]
)
# print(basic_packet_check(pkt1))

pkt2 = bytearray(
    [
        0x46,
        0x0,
        0x0,
        0x1E,
        0x16,
        0x2E,
        0x0,
        0x0,
        0x40,
        0x6,
        0xCC,
        0x59,
        0x66,
        0x66,
        0x44,
        0x44,
        0x98,
        0x76,
        0x54,
        0x32,
        0x0,
        0x0,
        0x0,
        0x0,
        0x1,
        0x2,
        0x3,
        0x4,
        0x5,
        0x6,
    ]
)
# print(basic_packet_check(pkt2))

pkt3 = bytearray(
    [
        0x45,
        0x0,
        0x0,
        0x1B,
        0x12,
        0x67,
        0x20,
        0xE,
        0x20,
        0x6,
        0x35,
        0x58,
        0x66,
        0x66,
        0x44,
        0x44,
        0x55,
        0x44,
        0x33,
        0x22,
        0x11,
        0x0,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
    ]
)
# print(basic_packet_check(pkt3))


# def destination_address(packet):
#     """Takes a single bytearray parameter (representing an IPv4 packet)
#     and returns a tuple (addr, dd), where:
#     - addr is the 32-bit value of the destination address
#     - dd is a string in dotted decimal notation.
#     """
#     # first 4 bits of the first byte
#     version = packet[0] >> 4
#     if version != 4:
#         raise ValueError("Packet version number must equal 4")

#     addr = packet[16:20]
#     dd = ".".join(str(byte) for byte in addr)

#     return addr, dd


def destination_address(packet):
    """Extracts the IPv4 destination address from a packet and returns it in both 32-bit and dotted-decimal formats."""

    # bytes 16 to 19
    dest_ip_bytes = packet[16:20]

    # bytes to 32-bit integer
    addr = (
        (dest_ip_bytes[0] << 24)
        | (dest_ip_bytes[1] << 16)
        | (dest_ip_bytes[2] << 8)
        | dest_ip_bytes[3]
    )

    # bytes in dotted-decimal notation
    dd = f"{dest_ip_bytes[0]}.{dest_ip_bytes[1]}.{dest_ip_bytes[2]}.{dest_ip_bytes[3]}"

    return addr, dd


packet = bytearray(
    [
        0x45,
        0x00,
        0x00,
        0x1E,
        0x04,
        0xD2,
        0x00,
        0x00,
        0x40,
        0x06,
        0x00,
        0x00,
        0x00,
        0x12,
        0x34,
        0x56,
        0x33,
        0x44,
        0x55,
        0x66,
    ]
)
# print(destination_address(packet))


def payload(packet):
    """Takes a single bytearray parameter (representing an IPv4 packet)
    and returns just the packet's payload (as a bytearray).
    """
    hdr_len = packet[0] & 0x0F
    header_length = hdr_len * 4
    payload = packet[header_length:]
    return payload


packet = bytearray(
    [
        0x45,
        0x00,
        0x00,
        0x17,
        0x00,
        0x00,
        0x00,
        0x00,
        0x40,
        0x06,
        0x69,
        0x8D,
        0x11,
        0x22,
        0x33,
        0x44,
        0x55,
        0x66,
        0x77,
        0x88,
        0x10,
        0x11,
        0x12,
    ]
)
# print(payload(packet))


packet = bytearray(
    [
        0x46,
        0x00,
        0x00,
        0x1E,
        0x00,
        0x00,
        0x00,
        0x00,
        0x40,
        0x06,
        0x68,
        0x86,
        0x11,
        0x22,
        0x33,
        0x44,
        0x55,
        0x66,
        0x77,
        0x88,
        0x00,
        0x00,
        0x00,
        0x00,
        0x13,
        0x14,
        0x15,
        0x16,
        0x17,
        0x18,
    ]
)
# print(payload(packet))

# Don't forget to include the definition for the checksum function that you
# wrote for the previous question here!


def compose_packet(
    hdrlen,
    tosdscp,
    identification,
    flags,
    fragmentoffset,
    timetolive,
    protocoltype,
    sourceaddress,
    destinationaddress,
    payload,
):
    """Takes the values to be filled into the IPv4 header
    and also a bytearray containing the payload.
    Returns a bytearray of the entire IPv4 packet (header and payload).
    Raises an appropriate ValueError if a parameter is erroneous.
    """
    totallength = hdrlen * 4 + len(payload)
    version = 4
    headerchecksum = 0

    field_lengths = {
        "hdrlen": (hdrlen, 4),
        "tosdscp": (tosdscp, 6),
        "totallength": (totallength, 16),
        "identification": (identification, 16),
        "flags": (flags, 3),
        "fragmentoffset": (fragmentoffset, 13),
        "timetolive": (timetolive, 8),
        "protocoltype": (protocoltype, 8),
        "headerchecksum": (headerchecksum, 16),
        "sourceaddress": (sourceaddress, 32),
        "destinationaddress": (destinationaddress, 32),
    }
    if hdrlen < 5 or hdrlen > 15:
        raise ValueError("hdrlen must be at least 5 and no greater than 15")
    
    for key, (value, bits) in field_lengths.items():
        if value < 0 or value >= (1 << bits):
            raise ValueError(f"{key} value cannot fit in {bits} bits")

    # Constructing the header
    header = bytearray(hdrlen*4)

    # First byte: version and header length
    # When an extended header is required (i.e. when the hdrlen parameter is greater than 5),
    # then the additional 32-bit words making up the header options should be filled with zero bytes.

    header[0] = (version << 4) | hdrlen
    # print(header[0])

    # Second byte: TOS/DSCP
    header[1] = tosdscp << 2
    # print(header[1])

    # Third and fourth bytes: Total length
    header[2] = (totallength >> 8) & 0xFF
    header[3] = totallength & 0xFF

    # Fifth and sixth bytes: Identification
    header[4] = (identification >> 8) & 0xFF
    header[5] = identification & 0xFF

    # Seventh and eighth bytes: Flags and fragment offset
    header[6] = ((flags << 5) | (fragmentoffset >> 8)) & 0xFF
    header[7] = fragmentoffset & 0xFF

    # Ninth byte: Time to live
    header[8] = timetolive

    # Tenth byte: Protocol type
    header[9] = protocoltype

    # Eleventh and twelfth bytes: Header checksum - initially 0
    header[10] = 0
    header[11] = 0

    # Thirteenth to sixteenth bytes: Source address
    header[12] = (sourceaddress >> 24) & 0xFF
    header[13] = (sourceaddress >> 16) & 0xFF
    header[14] = (sourceaddress >> 8) & 0xFF
    header[15] = sourceaddress & 0xFF

    # Seventeenth to twentieth bytes: Destination address
    header[16] = (destinationaddress >> 24) & 0xFF
    header[17] = (destinationaddress >> 16) & 0xFF
    header[18] = (destinationaddress >> 8) & 0xFF
    header[19] = destinationaddress & 0xFF

    # If hdrlen > 5, fill the remaining bytes with zeros
    for i in range(20, hdrlen * 4):
        header[i] = 0

    headerchecksum = checksum(header)
    header[10] = (headerchecksum >> 8) & 0xFF
    header[11] = headerchecksum & 0xFF

    packet = header + payload

    return packet


packet = compose_packet(
    6,
    24,
    4711,
    0,
    22,
    64,
    0x06,
    0x22334455,
    0x66778899,
    bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15]),
)
print(packet.hex())

assert 4660001e1267001640061165223344556677889900000000101112131415 == 4660001e1267001640061165223344556677889900000000101112131415


try:
    compose_packet(16, 0, 4000, 0, 63, 22, 0x06, 2190815565, 3232270145, bytearray([]))
    print("hdrlen is too large")
except ValueError as err:
    print(err)
