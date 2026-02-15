import math


def number_fragments(
    message_size_bytes, overhead_per_packet_bytes, maximum_n_packet_size_bytes
):
    s = message_size_bytes
    o = overhead_per_packet_bytes
    m = maximum_n_packet_size_bytes
    if m <= o:
        raise ValueError("Packet size M must be greater than overhead O")
    payload_size = m - o
    return math.ceil(s / payload_size)


# Example usage:
# print(number_fragments(10000, 100, 1000))  # Output should be 12


def last_fragment_size(
    message_size_bytes, overhead_per_packet_bytes, maximum_n_packet_size_bytes
):
    # payload size per packet
    payload_size_per_packet = maximum_n_packet_size_bytes - overhead_per_packet_bytes

    # size of  last fragment
    last_fragment_size = message_size_bytes % payload_size_per_packet

    # If there's no remainder, the last fragment is a full-sized packet
    if last_fragment_size == 0:
        last_fragment_size = maximum_n_packet_size_bytes
    else:
        # Add the overhead to the last fragment size
        last_fragment_size += overhead_per_packet_bytes

    return last_fragment_size


# print(last_fragment_size(10000, 100, 1000))
# # 200
# print(last_fragment_size(160, 20, 100))
# # 100
# print(last_fragment_size(20, 20, 1500))


def fragment_offsets(fragment_size_bytes, overhead_size_bytes, message_size_bytes):
    # Calculate the payload size per fragment
    payload_size = fragment_size_bytes - overhead_size_bytes

    # Initialize the list of offsets
    offsets = []

    # Generate the offsets
    for offset in range(0, message_size_bytes, payload_size):
        offsets.append(offset)

    return offsets


print(fragment_offsets(1500, 40, 3000) == [0, 1460, 2920])
