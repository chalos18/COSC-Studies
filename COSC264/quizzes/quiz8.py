def dev_rtt(sample_rtts):
    alpha = 0.125
    beta = 0.25
    # Initialize EstimatedRTT with the first SampleRTT
    estimated_rtt = sample_rtts[0]
    dev_rtt = 0  # Initial DevRTT is zero

    for sample_rtt in sample_rtts:
        # Update EstimatedRTT
        estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sample_rtt
        # Update DevRTT
        dev_rtt = (1 - beta) * dev_rtt + beta * abs(sample_rtt - estimated_rtt)

    return dev_rtt


# print(f"{dev_rtt([1]):.3f}")
# print(f"{dev_rtt([1,1,1]):.3f}")
# print(f"{dev_rtt([1,2]):.3f}")
# print(f"{dev_rtt([1,2,3]):.3f}")


def timeout_interval(sample_rtts):
    alpha = 0.125
    beta = 0.25
    # Initialize EstimatedRTT with the first SampleRTT
    estimated_rtt = sample_rtts[0]
    dev_rtt = 0  # Initial DevRTT is zero

    for sample_rtt in sample_rtts:
        # Update EstimatedRTT
        estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sample_rtt
        # Update DevRTT
        dev_rtt = (1 - beta) * dev_rtt + beta * abs(sample_rtt - estimated_rtt)

    # Calculate TimeoutInterval
    timeout_interval = estimated_rtt + 4 * dev_rtt

    return timeout_interval


# print(f"{timeout_interval([1]):.3f}")  # Output: 1.000
# print(f"{timeout_interval([1, 1]):.3f}")  # Output: 1.000
# print(f"{timeout_interval([1, 2]):.3f}")  # Output: 2.000
# print(f"{timeout_interval([1, 2, 3]):.3f}")  # Output: 3.656


def num_rtt(initial, ssthresh):
    cong_win = initial  # Start with the initial congestion window
    rtt_count = 0  # Number of round trips

    while cong_win <= ssthresh:
        rtt_count += 1
        cong_win *= 2  # Double the congestion window each round trip

    return rtt_count


print(num_rtt(1, 16))  # Output: 5
print(num_rtt(2, 16))  # Output: 4
