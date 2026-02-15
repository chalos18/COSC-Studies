import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 6 * np.pi  # Carrier frequency in radians per second
T = 1  # Duration of one bit
f0 = 0  # Frequency for binary '0'
f1 = 4 * np.pi  # Frequency for binary '1'
A = 1  # Amplitude
bit_duration = T  # Duration of each bit
sampling_rate = 1000  # Sampling rate for the signal


# Time axis
t = np.linspace(
    0, len("10110001") * bit_duration, len("10110001") * bit_duration * sampling_rate
)


# Generate waveform
data = "10110001"
signal = np.zeros(len(t))

for i, bit in enumerate(data):
    start = i * bit_duration * sampling_rate
    end = (i + 1) * bit_duration * sampling_rate
    if bit == "1":
        freq = f1
    else:
        freq = f0
    time_segment = t[int(start) : int(end)]
    signal[int(start) : int(end)] = A * np.sin(2 * np.pi * freq * time_segment)


# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="FSK Modulated Signal")
plt.title("FSK Modulated Signal for Data Sequence 10110001")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
