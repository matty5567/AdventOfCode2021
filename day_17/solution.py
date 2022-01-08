import re
from itertools import combinations
from operator import add

def parse_input(raw_in):
    print(raw_in)
    intermed = re.findall("-?\d+", raw_in)
    return [int(i) for i in intermed]

def calc_position(init_x, init_y, steps):
    vel_x, vel_y = init_x, init_y
    pos_x, pos_y = 0, 0
    for _ in range(steps):
        pos_x, pos_y = pos_x + vel_x, pos_y + vel_y
        vel_x, vel_y = max(vel_x-1, 0), vel_y-1
    return (pos_x, pos_y)
    

def calc_max_height(y1, y2):

    nums = [(i*(i+1)/2, i) for i in range(1000)]
    options = list(combinations(nums, 2))
    viable = sorted([i for i in options if abs(y2)  <= abs(i[1][0]-i[0][0]) <= abs(y1)], key= lambda x:x[0][0])
    return viable[-1]


def valid_throw(init_x, init_y, x1, x2, y1, y2):
    pos = (0, 0)
    steps = 1
    while pos[0] < max(x1, x2) and pos[1] > min(y1, y2):
        pos = calc_position(init_x, init_y, steps)
        steps += 1
        if x1 <= pos[0] <= x2 and y2 >= pos[1] >= y1:
            return True

    return False


def find_valid_vels(x1, x2, y1, y2):
    valid_throws = []
    for x in range(0, x2+1):
        for y in range(y1, 150):
            if valid_throw(x, y, x1, x2, y1, y2):    
                valid_throws.append((x, y))
    return valid_throws


if __name__=="__main__":
    with open('data.txt') as f:

         x1, x2, y1, y2 = parse_input(f.read())
         print(find_valid_vels(x1, x2, y1, y2))
