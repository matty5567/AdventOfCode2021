from itertools import pairwise, permutations
from  math import floor, ceil
from ast import literal_eval

def explode(num):
    ctr = 0
    pos_last_dig = None
    split_pos = None
    for pos, i in enumerate(num):
        if ctr == 4 and i == "[" and not split_pos:
            if pos_last_dig:
                num[pos_last_dig] = str(int(num[pos_last_dig]) + int(num[pos+1]))
            new_num = int(num[pos+3])
            split_pos = pos


        elif i == "[":
            ctr += 1
        elif i == "]":
            ctr -= 1
            
        elif i.isdigit():
            if split_pos and pos > split_pos + 4:
                num[pos] = str(int(num[pos]) + new_num)
                break
            else:
                pos_last_dig = pos

            
    if split_pos:   
        return num[:split_pos] + ["0"] + num[split_pos + 5:], True

    else:
         return num, False


def split(num):
    j = None
    for pos, i in enumerate(num):
        if i.isdigit() and int(i) > 9:
            j = int(i)
            num = num[:pos] + ["[", str(floor(j/2)), ",", str(ceil(j/2)), "]"] + num[pos + 1:] 
            break

    return num, bool(j)

def reduce(num):
    while True:
        num, exploded = explode(num)
        if exploded:
            continue
        num, has_split = split(num)
        if not exploded and not has_split:
            return "".join(num)


def magnitude(num):
    if isinstance(num, int):
        return num

    return 3 * magnitude(num[0]) + 2 * magnitude(num[-1])
        


if __name__=="__main__":
    with open('data.txt') as f:
        numbers = map(lambda x: x.strip(), f.readlines())
        max_mag = 0
        for ctr, i in enumerate(permutations(numbers, 2)):
            if ctr % 100 == 0:
                print(ctr)
            total = magnitude(literal_eval(reduce(list("[" + i[0] +  "," + i[1]  + "]"))))
            if total > max_mag:
                max_mag = total

        print(max_mag)
