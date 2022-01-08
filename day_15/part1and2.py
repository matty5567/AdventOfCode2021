import numpy as np

class board:
    def __init__(self, board, part=1):
        self.board = board
        if part == 2:
            self.build_full_board()

        self.visited_nodes = np.zeros(self.board.shape)
        self.target = self.board.shape[0]-1, self.board.shape[0]-1
        self.A_star()

    def build_full_board(self):
        full_board = np.zeros((self.board.shape[0]*5, self.board.shape[0]*5))
        for k in np.ndindex(self.board.shape):
            for i in range(5):
                for j in range(5):
                    assigned_risk = (self.board[k] + i + j) % 9
                    full_board[k[0] + i*self.board.shape[0], k[1] + j*self.board.shape[1]] = 9 if assigned_risk == 0 else assigned_risk

        self.board = full_board

    def calc_heuristic_dist(self, position):
        return np.sqrt((self.target[0] - position[0])**2 + (self.target[1] - position[1])**2)

    def A_star(self):
        curr_y, curr_x = (0,0)
        curr_cost = 0
        
        options = {}
        while (curr_y, curr_x) != self.target:
            self.visited_nodes[curr_y, curr_x] = 1
            for new_y, new_x in [(curr_y + 1, curr_x), (curr_y, curr_x + 1), (curr_y - 1, curr_x), (curr_y, curr_x - 1)]:
                if self.board.shape[1] > new_x >= 0 <= new_y < self.board.shape[0] and self.visited_nodes[new_y, new_x] != 1:
                    new_cost = curr_cost + self.board[new_y, new_x]
                    options[(new_y, new_x)] = min(options.get((new_y, new_x), 1000), new_cost)
            
            curr_y, curr_x = sorted(options.items(), key=lambda item: item[1] + self.calc_heuristic_dist(item[0]))[0][0]
            curr_cost = options.pop((curr_y, curr_x))
            print(options, curr_y, curr_x)
        print("shortest path is: ", curr_cost)
        return curr_cost
                


if __name__ == "__main__":
    with open("test_data.txt") as f:
        data = f.readlines()
        board = board(np.array(list(map(lambda x: [int(i) for i in x.strip()], data))))
        