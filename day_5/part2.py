import itertools
import numpy as np

with open(r'day_5\data.txt') as f:
    lines = [[int(j[0].split(',')[0]), int(j[0].split(',')[1]), int(j[1].split(',')[0]), int(j[1].split(',')[1].strip())] for j in [i.split(" -> ") for i in f.readlines()]]
    max_value = max(itertools.chain(*lines)) +1
    map = np.zeros((max_value, max_value))
    
    for line in lines:
        x1, y1, x2, y2 = line

        x_step = {0:-1, 1:1}[bool(x2>x1)]
        y_step = {0:-1, 1:1}[bool(y2>y1)]

        x_vals = list(range(x1, (x2 + 1 if x_step > 0 else (x2 - 1)), x_step))
        y_vals = list(range(y1, (y2 + 1 if y_step > 0 else (y2 - 1)), y_step))

        if len(x_vals) > len(y_vals):
            line_points = list(zip(x_vals, itertools.cycle(y_vals)))

        else:
            line_points = list(zip(itertools.cycle(x_vals), y_vals))

        for i, j in line_points:
            map[j, i] += 1

    print(map)
    print(np.count_nonzero(map >= 2))