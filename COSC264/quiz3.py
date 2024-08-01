def connection_setup_delay(
    cable_length_km,
    light_speed_kmps,
    message_length_b,
    data_rate_bps,
    processing_time_s,
):
    d = cable_length_km
    c = light_speed_kmps
    m = message_length_b
    r = data_rate_bps
    p = processing_time_s

    propagation_delay = d / c
    transmission_delay = m / r
    processing_delay = p

    total_delay = 4 * (propagation_delay + transmission_delay + processing_delay)

    return total_delay


# print(f"{connection_setup_delay(10000, 200000, 4000, 1000000, 0.001):.2f}")


def message_delay(
    conn_setup_time_s,
    cable_length_km,
    light_speed_kmps,
    message_length_b,
    data_rate_bps,
):
    ts = conn_setup_time_s
    d = cable_length_km
    c = light_speed_kmps
    m = message_length_b
    r = data_rate_bps

    propagation_delay = d / c
    transmission_delay = m / r

    total_delay = ts + 2 * propagation_delay + transmission_delay

    return total_delay


# print(f"{message_delay(0.2, 10000, 2000000, 1000, 1000000):.3f}")

import math


import math


def total_number_bits(
    max_user_data_per_packet_b, overhead_per_packet_b, message_length_b
):
    """Calculates the total number of bits required to transmit a message in packets.

    Args:
      max_user_data_per_packet_b: Maximum number of user data bits per packet.
      overhead_per_packet_b: Number of overhead bits per packet.
      message_length_b: Length of the message in bits.

    Returns:
      Total number of bits required to transmit the message.
    """

    s = max_user_data_per_packet_b
    o = overhead_per_packet_b
    m = message_length_b

    # Calculate the number of full packets
    num_full_packets = math.floor(m / s)

    # Calculate the number of bits in the last packet
    last_packet_bits = m % s

    # Calculate total bits
    total_bits = num_full_packets * (s + o)
    if last_packet_bits > 0:
        total_bits += last_packet_bits + o
    return total_bits


# print(f"{total_number_bits(1000, 100, 10000):.0f}")
# print(f"{total_number_bits(1000, 100, 10001):.0f}")


def packet_transfer_time(
    link_length_km,
    light_speed_kmps,
    processing_delay_s,
    data_rate_bps,
    max_user_data_per_packet_b,
    overhead_per_packet_b,
):
    d = link_length_km
    c = light_speed_kmps
    p = processing_delay_s
    r = data_rate_bps
    s = max_user_data_per_packet_b
    o = overhead_per_packet_b

    propagation_delay = d / c
    transmission_delay = (s + o) / r
    processing_delay = p

    total_transfer_time = 2 * (
        propagation_delay + transmission_delay + processing_delay
    )

    return total_transfer_time


# print(f"{packet_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100):.4f}")


def total_transfer_time(
    link_length_km,
    light_speed_kmps,
    processing_delay_s,
    data_rate_bps,
    max_user_data_per_packet_b,
    overhead_per_packet_b,
    message_length_b,
):
    d = link_length_km
    c = light_speed_kmps
    p = processing_delay_s
    r = data_rate_bps
    s = max_user_data_per_packet_b
    o = overhead_per_packet_b
    m = message_length_b

    num_packets = m // s

    # Calculate individual delays
    propagation_delay = d / c
    transmission_delay = (s + o) / r

    # Total transfer time considering pipelining
    total_time = (
        2 * propagation_delay
        + transmission_delay
        + p
        + (transmission_delay) * (num_packets)
        + p
    )

    return total_time


# Once you've worked that out, you should be able to use that, plus your answer
# to a previous question and your calculation for the total number of packets, to solve Question 9.
# print(f"{total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000):.4f}")
