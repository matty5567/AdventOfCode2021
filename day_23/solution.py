from tqdm import tqdm
import numpy as np
from multiprocessing import Pool

class Hotel:
    def __init__(self):
        self.costs = {}
        self.positions = {"A1":(1, 4), "A2":(2, 4), "B1":(2, 2), "B2":(1, 6),
                          "C1":(1, 2), "C2":(2, 8), "D1":(2, 6), "D2":(1, 8)}


        # self.positions = {"A1":(1, 2), "A2":(2, 2), "B1":(1, 4), "B2":(2, 4),
        #                   "C1":(1, 6), "C2":(2, 6), "D1":(2, 8), "D2":(0, 10)}

        self.target_x = {"A": 2, "B": 4, "C": 6, "D": 8}
        self.move_cost = {"A": 1, "B": 10, "C": 100, "D": 1000}


        self.find_least_move_cost_seed(self.positions)

    def show_map(self, positions):
        hotel_map = np.empty((3, 11), dtype='object')
        for i, pos in positions.items():
            hotel_map[pos] = i


        for j in range(11):
            if hotel_map[0, j]==None:
                if hotel_map[1, j] or hotel_map[2, j]:
                    hotel_map[0, j] = ". "
                else:
                    hotel_map[0, j] = "."

            
            if hotel_map[1, j] == None:
                    if hotel_map[2, j] == None:
                        hotel_map[1, j] = "."
                    else:
                        hotel_map[1, j] = ". "

            if hotel_map[2, j] == None:
                    if hotel_map[1, j] == ".":
                        hotel_map[2, j] = "."
                    else:
                        hotel_map[2, j] = ". "



        for k in [1, 2]:
            for j in range(11):
                if j%2 or j==0 or j==10:
                    if hotel_map[0, j] == ".":

                        hotel_map[k, j] = "#"
                    else:
                        hotel_map[k, j] = "# "

        print(np.array2string(hotel_map))


    @staticmethod
    def calc_journey(start, end):
        intermed_pos = []

        if start[0] > 0:
            intermed_pos += [(i, start[1]) for i in range(1, start[0]+1)]

        if end[0] > 0:
            intermed_pos += [(i, end[1]) for i in range(1, end[0]+1)]

        if start[1] < end[1]:
            intermed_pos += [(0, i) for i in range(start[1], end[1]+1)]

        else:
            intermed_pos += [(0, i) for i in range(end[1], start[1]+1)]

        intermed_pos.remove(start)

        return intermed_pos


    def legal_move(self, start, end, piece, positions):

        # once in hallway stays till can move into its room
        if (start[0] == 0 and end[0] == 0):
            return False, None

        # if piece in position, dont move it
        if start == (2, self.target_x[piece[0]]):
            return False, None

        if start == (1, self.target_x[piece[0]]) and positions[piece[0]+{"1":"2", "2": "1"}[piece[1]]] == (2, start[1]):
            return False, None


        if end[0] == 1 and (2, end[1]) not in positions.values():
            return False, None

        # never stop outside room
        if end[0] == 0 and (1 < end[1] < 10) and (not end[1] % 2):
            return False, None
            # print("never stop outside room")

        # never stop in room unless theres and no other types inside
        if end[0] > 0:
            if end[1] != self.target_x[piece[0]]:
                return False, None

            # if piece of other type in room
            if [p for p, pos in positions.items() if pos[1]==end[1] and p[0]!=piece[0]]:
                return False, None

        if (start[0], end[0]) in [(1, 2), (2, 1)]:
            return False, None

        journey = self.calc_journey(start, end)

        # piece in way
        if [i for i in journey if i in positions.values()]:
            return False, None
            # print(piece, "piece in the way at: ", x, " from ", start, " to ", end)

        return True, len(journey)*self.move_cost[piece[0]]


    def find_all_next_positions(self, positions):
        
        moves = []
        end_locs = [(0, i) for i in range(11)] + [(j, k) for j in [1, 2] for k in [2, 4, 6, 8]]
        for piece, pos in positions.items():
            for end in end_locs:
                legal, cost = self.legal_move(pos, end, piece, positions)
                if legal:
                    moves.append((self.make_move(piece, end, dict(positions)), cost))
        return moves

    def is_completed(self, positions):
        return all([pos[1] == self.target_x[piece[0]] for piece, pos in positions.items()])

    @staticmethod
    def make_move(piece, end, pos):
        pos[piece] = end
        return pos

    def find_least_move_cost_seed(self, positions):
        moves = self.find_all_next_positions(positions)
        with Pool(10) as p:
            costs = p.map(self.find_least_move_cost, [(pos, cost) for pos, cost in moves])
        print(min(costs))



    def find_least_move_cost(self, x):
        positions, cost = x
        if cost > 13000:
            return 13000

        if self.is_completed(positions):
            return cost

        moves = self.find_all_next_positions(positions)

        if not moves:
            return 13000
            
        return min([self.find_least_move_cost((pos, cost+c)) for pos, c in moves])



if __name__ == '__main__':
    hotel = Hotel()





