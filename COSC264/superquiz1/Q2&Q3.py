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
    """Takes a single bytearray parameter (representing an IPv4 packet)
    and returns True if it passes all the basic correctness checks.
    Raises an appropriate ValueError if any of the correctness checks fail.
    """

    packet_len = len(packet)
    if packet_len < 20:
        raise ValueError("Packet does not contain a full IP header")

    for i in range(0, packet_len):
        # Extract 16-bit integer from the header
        # Big-endian: higher byte first
        byte1 = packet[i]  # First byte of the 16-bit number
        version_number = byte1 << 4

    print(version_number)


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
print(basic_packet_check(pkt1))

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
