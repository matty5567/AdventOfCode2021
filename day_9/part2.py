import numpy as np

class basin():
    def __init__(self, low_point, _map):
        self.size = 1
        self.low_point = low_point
        self.points = [low_point]
        self.full = False
        self.num_points = 1
        self.maximise(_map)
        
    def find_neighbours(self, _map):
        y_size, x_size = _map.shape
        new_nbrs = []
        for point in self.points:
            i, j = point
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x_coord = j + x
                y_coord = i + y
                if 0 <= x_coord < x_size and 0 <= y_coord < y_size:
                    if ((y_coord, x_coord) not in self.points) and (_map[y_coord, x_coord] != 9):
                        new_nbrs.append((y_coord, x_coord))
        if not new_nbrs:
            self.full = True
        else:
            self.points += list(dict.fromkeys(new_nbrs))
            self.num_points = len(self.points)

    def maximise(self, _map):
        while not self.full:
            self.find_neighbours(_map)


def find_low_points(_map):
    y_size, x_size = _map.shape
    low_points = []
    for i in range(0, y_size):
        for j in range (0, x_size):
            element = _map[i, j]
            surrounding_elements = []
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x_coord = j + x
                y_coord = i + y
                if 0 <= x_coord < x_size and 0 <= y_coord < y_size:
                    surrounding_elements.append(_map[y_coord, x_coord])
            if element < min(surrounding_elements):
                low_points.append(basin((i, j), _map))
    return low_points


with open(r"day_9/data.txt") as f:
    _map = np.array([map(lambda x: int(x), i.strip()) for i in f.readlines()])
    basin_points = find_low_points(_map)

    top_three_basin_sizes = [i.num_points for i in sorted(basin_points, key=lambda x: x.num_points, reverse=True)[0:3]]

    print(np.prod(top_three_basin_sizes))
    


    

    