import numpy as np

with open(r"day_9/data.txt") as f:
    f = np.array([map(lambda x: int(x), i.strip()) for i in f.readlines()])
    y_size, x_size = f.shape
    low_points = []
    for i in range(0, y_size):
        for j in range (0, x_size):
            element = f[i, j]
            surrounding_elements = []
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x_coord = j + x
                y_coord = i + y
                if 0 <= x_coord < x_size and 0 <= y_coord < y_size:
                    surrounding_elements.append(f[y_coord, x_coord])
            if element < min(surrounding_elements):
                low_points.append(1 + element)
    print(sum(low_points))