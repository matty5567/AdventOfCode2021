import numpy as np

def board_winning(board):
    if (-5 in np.sum(board, axis = 0)) or (-5 in np.sum(board, axis = 1)):
        return True

with open(r'day_4\data.txt') as f:
    values, *cards = f.read().split('\n\n')

    boards = [np.array([list(map(lambda x: int(x), filter(lambda x:x!='', arr.split(' ')))) for arr in i.split('\n')]) for i in cards]
    numbers = [int(x) for x in values.split(',')]


    for num in numbers:

        boards = [np.where(board==num, -1, board) for board in boards]
        
        if (len(boards) == 1) and (board_winning(boards[0])):
            print("last winning board: ", boards[0])
            print('score: ', np.sum(boards[0], where=boards[0]!=-1)*num)

        
        
        for board in boards:
            boards = list(filter(lambda x:not board_winning(x), boards))

        


                


