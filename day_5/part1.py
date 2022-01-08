import itertools
import numpy as np

with open(r'day_5\data.txt') as f:
    lines = [[int(j[0].split(',')[0]), int(j[0].split(',')[1]), int(j[1].split(',')[0]), int(j[1].split(',')[1].strip())] for j in [i.split(" -> ") for i in f.readlines()]]
    max_value = max(itertools.chain(*lines)) +1
    map = np.zeros((max_value, max_value))
    
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                map[j, x1] += 1

        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2)+1):
                map[y1, j] += 1

    print(map)
    print(np.count_nonzero(map >= 2))