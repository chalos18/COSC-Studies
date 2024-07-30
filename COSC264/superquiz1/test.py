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

    if version != 4:
        raise ValueError("version field must be 4")

    for key, (value, bits) in field_lengths.items():
        if value < 0 or value >= (1 << bits):
            raise ValueError(f"{key} value cannot fit in {bits} bits")

    # Constructing the header
    header = bytearray(20)

    # First byte: version and header length
    header[0] = (version << 4) | hdrlen

    # Second byte: TOS/DSCP
    header[1] = tosdscp

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


# Example usage
header = compose_header(4, 5, 24, 30, 1234, 0, 0, 64, 6, 8276, 305419896, 2557891634)
print(len(header))
print([byte for byte in header])  # Print byte values as a list for better clarity
