from itertools import chain
import numpy as np

class instructions():
    def __init__(self, positions, fold_instructions):
            self.size_of_array = (max(i[1] for i in positions) + 1, max(i[0] for i in positions) + 1)
            self.paper = np.zeros(self.size_of_array)
            for i in positions:
                self.paper[i[1], i[0]] = 1
            self.fold_instructions = [(i[i.index("=")-1], int(i[i.index("=")+1:])) for i in fold_instructions]
            self.execute_folds()

    def fold(self, axis, position):
        self.size_of_array = (self.size_of_array[0], position) if axis == "x" else (position, self.size_of_array[1])
        new_paper = np.zeros(self.size_of_array)

        for i in np.ndindex(self.size_of_array):
            x_val, y_val = 2*position - i[1], 2*position - i[0]

            if axis == "x" and (x_val < self.paper.shape[1]):
                new_paper[i] = max(self.paper[i], self.paper[i[0], x_val])

            elif axis == "y" and (y_val < self.paper.shape[0]):
                new_paper[i] = max(self.paper[i], self.paper[y_val, i[1]])
            else:
                new_paper[i] = self.paper[i]
        self.paper = new_paper

    def execute_folds(self):
        for axis, position in self.fold_instructions:
            self.fold(axis, position)
            
        print(self.paper)

if __name__ == "__main__":

    np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))


    with open(r'day_13/data.txt') as f:

        data = f.read().split("\n")
        positions = list(map(lambda x: [int(i) for i in x.split(',')], data[:data.index('')]))
        fold_instructions = data[data.index('')+1:]
        
        instructions(positions, fold_instructions)
    
