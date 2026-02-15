def convert(unsigned_int_x, base):
    x_type = type(unsigned_int_x)
    base_type = type(base)

    if x_type != int:
        raise TypeError("x is not an integer")
    if base_type != int:
        raise TypeError("base is not an integer")
    if unsigned_int_x < 0:
        raise ValueError("x must be positive")
    if base < 2:
        raise ValueError("base cannot be less than 2")

    result_list = []

    while unsigned_int_x > 0:
        remainder = unsigned_int_x % base
        result_list.append(remainder)

        # Repeatedly divide the number x by the base b
        unsigned_int_x = unsigned_int_x // base

    # Reverse the list to get the highest-order coefficient first
    result_list.reverse()

    return result_list


# print(convert(1234, 10))
# print(convert(4660, 16))


def hexstring(x):
    """
    Converts an unsigned integer x into a string representing the hexadecimal representation of x
    """
    x_type = type(x)

    if x_type != int:
        raise TypeError("x is not an integer")
    if x < 0:
        raise ValueError("x must be positive")
    # Convert the integer to hexadecimal representation
    hex_digits = "0123456789ABCDEF"
    coefficients = convert(x, 16)  # Get base-16 (hexadecimal) coefficients
    print(coefficients)

    # Build the hexadecimal string
    hex_string = "0x" + "".join(hex_digits[digit] for digit in coefficients)

    return hex_string


# print(hexstring(1234))
def decodedate(x):
    # Extract the month
    month = (x & 0xF0000000) >> 28

    # Extract the day
    day = (x & 0x0F800000) >> 23

    # Extract the year
    year = x & 0x007FFFFF

    # Format the result as 'dd.mm.yyyy'
    return f"{day}.{month}.{year}"


# Example usage:
# print(decodedate(1375733729))  # Output: 4.5.2017


def encodedate(day, month, year):
    # Check validity of inputs
    if not (1 <= month <= 12):
        raise ValueError("invalid month")
    if not (1 <= day <= 31):
        raise ValueError("invalid day")
    if not (0 <= year <= 2**23 - 1):
        raise ValueError("invalid year")

    # Encode month (4 bits)
    m_encoded = (month & 0xF) << 28

    # Encode day (5 bits)
    d_encoded = (day & 0x1F) << 23

    # Encode year (23 bits)
    y_encoded = year & 0x7FFFFF

    # Combine all fields
    encoded_value = m_encoded | d_encoded | y_encoded

    return encoded_value


# Example usage
# print(encodedate(4, 5, 2017))  # Example test


def transmission_delay(packet_length_bytes, rate_mbps):
    r = rate_mbps * 1000000  # Convert Mbps to bps
    l = packet_length_bytes
    transmission_delay = (l * 8) / r
    delay_milliseconds = transmission_delay * 1000
    return delay_milliseconds


# print(f"{transmission_delay(1000 , 10):.3f}")


def transmission_delay(packet_length_bytes, rate_mbps):
    r = rate_mbps * 1000000000  # Convert Gbps to bps
    l = packet_length_bytes
    transmission_delay = (l * 8) / r
    delay_milliseconds = transmission_delay * 1000
    return delay_milliseconds


# print(f"{transmission_delay(1000 , 10):.4f}")


def total_time(cable_length_km, packet_length_b):
    d = cable_length_km  # In km/s
    l = packet_length_b  # In bits
    return (l * 8) / d


# print(f"{total_time(10000, 8000):.4f}")


""" 
    To calculate the total time required for a packet to be completely transmitted and received
    over a communication cable, we need to consider both the transmission time and the 
    propagation delay.

    Transmission Time: Time taken to put all the bits of the packet onto the cable.
        - Transmission time = Packet lenght (bits) / Data Rate (bps)
    
    Propagation Delay: Time taken for a bit to travel from the transmitter to the receiver.
        - Propagation Delay = Cable Length (km) / Propagation Speed (km/s)
    
    Total Time = Transmission Time + Propagation Delay

    Total time to milliseconds = total_time_seconds * 1000
"""


def total_time(cable_length_km, packet_length_b):
    # Constants
    propagation_speed_km_per_s = 200000  # speed of light in the cable in km/s
    data_rate_bps = 10_000_000_000  # data rate in bits per second (10 Gbps)

    # Calculate transmission time in seconds
    transmission_time_s = packet_length_b / data_rate_bps

    # Calculate propagation delay in seconds
    propagation_delay_s = cable_length_km / propagation_speed_km_per_s

    # Calculate total time in seconds
    total_time_s = transmission_time_s + propagation_delay_s

    # Convert total time to milliseconds
    total_time_ms = total_time_s * 1000

    return total_time_ms


# Test example
# print(f"{total_time(10000, 8000):.4f}")


def queueing_delay(rate_bps, num_packets, packet_length_b):
    r = rate_bps
    n = num_packets
    l = packet_length_b

    waiting_time_s = (n * l) / r

    return waiting_time_s


# print(f"{queueing_delay(1000000, 7, 10000):.3f}")


def queueing_delay(rate_bps, num_packets, packet_length_b):
    r = rate_bps * 1000000  # Mbps to bps, there are 1000000 bps in one Mbps
    n = num_packets
    l = packet_length_b * 8  # Byte to bits, there are 8 bits in one byte

    waiting_time_s = (n * l) / r

    waiting_time_ms = waiting_time_s * 1000

    return waiting_time_ms


# print(f"{queueing_delay(100, 20, 1500):.2f}")


def average_trials(p_loss):
    probability = 1 - p_loss  # Probability of success
    avg_trials = 1 / probability  # avg number of trials needed

    return avg_trials


# print(f"{average_trials(0.1):.2f}")


def average_trials(p_loss):
    """
    - Suppose the transmitter wants to transmit 1,000 packets
    over a channel with a packet loss probability of P = 0.2
    - What is the average total number of packet transmission trials
    that the transmitter has to make?
    """
    probability = 1 - p_loss  # Probability of success
    avg_trials = 1000 / probability  # avg number of trials needed

    return avg_trials


# print(f"{average_trials(0.2):.2f}")


def per_from_ber(bit_error_probability, packet_len_b):
    p = bit_error_probability
    l = packet_len_b

    bit_error_prob = 1 - (1 - p) ** l
    return bit_error_prob


# print(f"{per_from_ber(0.0001, 1000):.3f}")


def avg_trials_from_ber(bit_error_probability, packet_length_b):
    p = bit_error_probability
    l = packet_length_b

    bit_error_prob = (1 - p) ** l
    avg_trials = 1 / bit_error_prob  # avg number of trials needed

    return avg_trials


# print(f"{avg_trials_from_ber(0.001, 2000):.3f}")
