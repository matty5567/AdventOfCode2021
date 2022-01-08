

def get_rating(readings, oxygen = True):

    
    counter = 0

    while len(readings) != 1:
        bit_lists = list(zip(*[i for i in readings]))
        if oxygen:
            significant_bit = int(bit_lists[counter].count('1') >= len(bit_lists[counter])/2)

        else:
            significant_bit = int(bit_lists[counter].count('1') < len(bit_lists[counter])/2)


        readings = list(filter(lambda x:x[counter]==str(significant_bit), readings))
        counter += 1

    return int(readings[0], 2)

with open(r'day_3\data.txt') as f:
        data = f.readlines()
        
        oxy = get_rating(data, True)
        co = get_rating(data, False)

        print(oxy * co)

