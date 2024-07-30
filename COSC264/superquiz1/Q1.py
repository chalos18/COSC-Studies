# array_size = 5
# my_array = bytearray(array_size)
# my_array[0] = 7  # sets the first byte to 7
# my_array[1:3] = [8, 9]  # sets the next two bytes to 8 and 9 respectively


def compose_header(
    version,
    hdrlen,
    tosdscp,
    totallength,
    identification,
    flags,
    fragmentoffset,
    timetolive,
    protocoltype,
    headerchecksum,
    sourceaddress,
    destinationaddress,
):
    """Takes the values to be filled into the IPv4 header
    and returns a 20-byte bytearray of the standard IPv4 header.
    Raises an appropriate ValueError if a parameter is erroneous.
    """
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

    # if version != 4:
    # raise ValueError("version field must be 4")
    # for key in field_lengths:
    #     if field_lengths[key][0] < 0 or field_lengths[key][0] > (
    #         (2 ** (field_lengths[key][1]))
    #     ):
    #         raise ValueError(f"{key} value cannot fit in {field_lengths[key][1]} bits")
    if version != 4:
        raise ValueError("version field must be 4")

    for key, (value, bits) in field_lengths.items():
        if value < 0 or value >= (1 << bits):
            raise ValueError(f"{key} value cannot fit in {bits} bits")

    # Constructing the header
    header = bytearray(20)

    # First byte: version and header length
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

    # Eleventh and twelfth bytes: Header checksum
    header[10] = (headerchecksum >> 8) & 0xFF
    header[11] = headerchecksum & 0xFF

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

    return header


# try:
#     compose_header(4, 16, 0, 4000, 24200, 0, 63, 22, 6, 4711, 2190815565, 3232270145)
#     print("hdrlen value is too large")
# except ValueError as err:
#     print(err)

header = compose_header(
    4, 5, 0, 1500, 24200, 0, 63, 22, 6, 4711, 2190815565, 3232270145
)
print(header.hex())
assert (str(header.hex())) == "450005dc5e88003f160612678295314dc0a88741"

# header = compose_header(4, 5, 24, 30, 1234, 0, 0, 64, 6, 8276, 305419896, 2557891634)
# print(header)
# print(header.hex())
# for byte in header:
#     print(byte)

# try:
#     compose_header(
#         4, 15, 63, 65535, 65535, 7, 8191, 255, 255, 65535, 4294967295, 4294967296
#     )
#     print("destinationaddress is too big")
# except ValueError as err:
#     print(err)

# try:
#     compose_header(5, 5, 0, 4000, 24200, 0, 63, 22, 6, 4711, 2190815565, 3232270145)
#     print("version is 5")
# except ValueError as err:
#     print(err)

# try:
#     compose_header(4, 16, 0, 4000, 24200, 0, 63, 22, 6, 4711, 2190815565, 3232270145)
#     print("hdrlen value is too large")
# except ValueError as err:
#     print(err)
