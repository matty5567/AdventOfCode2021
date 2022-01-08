import numpy as np

with open(r'day_7\data.txt') as f:
    positions = [int(x) for x in f.read().split(",")]
    optimal_x = np.median(positions)
    total_fuel = np.sum([abs(i - optimal_x) for i in positions])
    print(total_fuel)