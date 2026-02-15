import csv
from math import log2
from collections import defaultdict

data = defaultdict(list)

# Step 1: Read file into (A, W) → times
with open("experiment_ana.txt", "r") as experiment:
    for line in experiment:
        parts = line.strip().split()
        if len(parts) >= 5:
            a = float(parts[1])
            w = float(parts[2])
            time_ms = float(parts[4])
            data[(a, w)].append(time_ms / 1000)  # ms → s

# Step 2: Group by ID
id_grouped = defaultdict(list)
for (a, w), times in data.items():
    times = times[2:]  # remove outliers
    mean_time = sum(times) / len(times)
    ID = log2(a / w + 1)
    id_grouped[ID].append(mean_time)

# Step 3: Write summary.csv (one row per ID)
with open("summary2.csv", "w", newline="") as csvfile:
    fieldnames = ["ID", "Mean time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for ID in sorted(id_grouped.keys()):
        mean_time = sum(id_grouped[ID]) / len(id_grouped[ID])
        writer.writerow({"ID": f"{ID:.3f}", "Mean time": f"{mean_time:.3f}"})
