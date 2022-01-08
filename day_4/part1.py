import numpy as np

with open(r'day_4\data.txt') as f:
    values, *cards = f.read().split('\n\n')

    boards = [np.array([list(map(lambda x: int(x), filter(lambda x:x!='', arr.split(' ')))) for arr in i.split('\n')]) for i in cards]
    numbers = [int(x) for x in values.split(',')]


    for num in numbers:
        boards = [np.where(board==num, -1, board) for board in boards]

        _break = False
        for board in boards:
            if (-5 in np.sum(board, axis = 0)) or (-5 in np.sum(board, axis = 1)):
                winning_board = board
                winning_num = num
                _break = True

        if _break:
            print(winning_board)
            print('score: ', np.sum(winning_board, where=winning_board!=-1)*winning_num)
            break
