import numpy as np

class Board:
    def __init__(self, board):
        self._board = board
        self.width = board.shape[1]
        print(self.simulate())
    
    def step(self, direction):
        move_count = 0
        east = direction == "east"
        piece = 1 if east else 2

        cur_board = self._board if east else np.transpose(self._board)
        new_board = np.zeros_like(cur_board)

        for row_num, row in enumerate(cur_board):
            for col_num, _ in enumerate(row):
                new_pos = (col_num + 1) % (self._board.shape[1] if east else self._board.shape[0])
                if row[col_num] == piece and row[new_pos] == 0:
                    move_count += 1
                    new_board[row_num, new_pos] = piece
                    new_board[row_num, col_num] = 0
                else:
                    new_board[row_num, col_num] = new_board[row_num, col_num] or row[col_num]

        self._board = new_board if east else np.transpose(new_board)
        return move_count


    def simulate(self):
        ctr = 0
        while True:
            ctr += 1
            east_moves = self.step("east")
            west_moves = self.step("south")

            if not (east_moves + west_moves):
                break

        return ctr


if __name__ == "__main__":
    with open("data.txt") as f:
        data = np.array(list(map(lambda x: [{".":0, ">": 1, "v": 2}[i] for i in x.strip()], f.readlines())))
        board = Board(data)

