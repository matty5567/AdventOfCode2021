import numpy as np

def calc_cost(x, positions):
    return np.sum([(abs(i - x) * (abs(i - x) + 1)/2) for i in positions])


with open(r'day_7\data.txt') as f:
    positions = [int(x) for x in f.read().split(",")]
    posible_xs = list(range(min(positions), max(positions)))
    least_cost =  sorted([(x, calc_cost(x, positions)) for x in posible_xs], key=lambda x:x[1])[0]
    print(least_cost)
    
    #print(optimal_x, total_fuel)