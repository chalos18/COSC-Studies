import math


def number_fdma_channels(b, g, u):
    n = (b - g) / (u + g)
    return math.floor(n)


# 49
# print(number_fdma_channels(1000000, 200, 20000))

# System bandwidth b=1 MHz (1,000,000 Hz)
# Guard band g=1 kHz (1,000 Hz)
# User channel bandwidth u=30 kHz (30,000 Hz)
# print(number_fdma_channels(1000000, 1000, 30000))


def number_tdma_users(s_s, g_s, u_s):
    n = s_s / (u_s + g_s)
    return math.floor(n)


# Test the function
# print(number_tdma_users(1, 0.001, 0.008))  # Output: 111

# print(number_tdma_users(0.1, 0.001, 0.005))  # Output: 111


def p_persistent_csma_collision_probability(p: float) -> float:
    """
        Consider the same setting as in the previous question, but now with p-persistent CSMA for some probability value 0 < p < 1. Please find an expression for the probability that both contenders collide. Assume that they are statistically independent. You will need to:

        - work out the probability that they collide in the first time slot, 
        the probability that they collide in the second time slot, 
        the probability that they collide in the k-th time slot, etc.;
        - combine these probabilities using the law of total probability; and
        - when calculating the end result, you will need the sum formula for the (infinite) geometric series.
    """
    if p <= 0 or p >= 1:
        raise ValueError("p must be between 0 and 1 (exclusive).")
    return p**2 / (2 * p - p**2)


# 0.111
# print(f"{p_persistent_csma_collision_probability(0.2):.3f}")


def p_persistent_csma_access_delay(p: float) -> float:
    if not (0 < p < 1):
        raise ValueError("p must be in the range (0, 1)")
    return (1 - p) / p


# Example usage
# print(f"{p_persistent_csma_access_delay(0.1):.3f}")  # Should print 9.000


def aggregate_throughput(n: int) -> float:
    # Each station has a throughput of 10 Gbps
    throughput_per_station = 10  # Gbps
    # Calculate the total aggregate throughput
    total_throughput = throughput_per_station * n
    return total_throughput


# Example usage
print(
    f"Aggregate throughput for 5 stations: {aggregate_throughput(5)} Gbps"
)  # Should print 50 Gbps
