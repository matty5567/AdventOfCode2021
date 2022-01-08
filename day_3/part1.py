from statistics import mode

with open(r'day_3\data.txt') as f:
    bit_lists = zip(*[i for i in f.readlines()])
    most_common_bits = [int(mode(i)) for i in bit_lists]
    least_common_bits = [1-i for i in most_common_bits]

    gamma = int(''.join([str(i) for i in most_common_bits]), 2)
    epsilon = int(''.join([str(i) for i in least_common_bits]), 2)

    print(gamma * epsilon)