import numpy as np
from itertools import chain

class cave:
    def __init__(self):
        self.num_flashes = 0

        with open(r'day_11/data.txt') as f:
            input_data = list(map(lambda x: [int(i) for i in x.strip()], f.readlines()))
            self._map = np.array(input_data)
            self.first_step_all_flash = None
            self.all_flashed = False
    @staticmethod
    def calc_nbrs(location):
        y, x = location
        nbrs = []
        for x_diff in [-1, 0, 1]:
            for y_diff in [-1, 0, 1]:
                x_loc = x + x_diff
                y_loc = y + y_diff
                if 0 <= x_loc < 10 and 0 <= y_loc < 10 and (x_diff, y_diff) != (0, 0):
                    nbrs.append((y_loc, x_loc))
        return nbrs
    
    def flash(self, full_energy):

        nbrs = chain(*[self.calc_nbrs(i) for i in full_energy])

        for i in full_energy:
            self.num_flashes += 1
            self._map[i] = 0
        for i in nbrs:
            if self._map[i] != 0:
                self._map[i] += 1

        while full_energy := list(zip(*np.where(self._map > 9))):
            self.flash(full_energy)
        

    def simulate(self, steps):
        
        for i in range(0, steps):
            self._map += 1                
            self.flash(list(zip(*np.where(self._map > 9))))

            if np.sum(self._map) == 0:
                self.first_step_all_flash = i + 1
    

    def find_first_time_all_zeros(self):
        counter = 0
        while np.sum(self._map) != 0:
            self._map += 1                
            self.flash(list(zip(*np.where(self._map > 9))))
            counter += 1
        return counter


            
oct_cave = cave()

print(oct_cave.find_first_time_all_zeros())


