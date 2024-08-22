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

print(number_tdma_users(0.1, 0.001, 0.005))  # Output: 111