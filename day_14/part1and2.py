from collections import Counter, defaultdict
from itertools import pairwise, chain


def calc_step(frequencies, letter_pairs):
    return_dict = defaultdict(int)
    for key, value in frequencies.items():
        if value > 0 and key in letter_pairs.keys():
            for i in letter_pairs[key]:
                return_dict[i] += value

        else:
            if key not in return_dict.keys():
                return_dict[key] = value

    return return_dict

def max_minus_min(frequencies, code):
    intermed_dict = defaultdict(int)
    for key, value in frequencies.items():
        for i in key:
            intermed_dict[i] += value

    intermed_dict[code[0]] += 1
    intermed_dict[code[-1]] += 1
    
    for key, value in intermed_dict.items():
        intermed_dict[key] = value / 2

    sorted_dict = sorted(intermed_dict.values())

    return(sorted_dict[-1] - sorted_dict[0])

if __name__ == "__main__":
    with open("data.txt") as f:
        code, _, *data = f.readlines()
        
        letter_pairs = {k:[k[0] + v, v + k[1]] for k,v in list(map(lambda x: x.strip().split(" -> "), data))}
        
        letter_freq = Counter(["".join(i) for i in pairwise(code.strip())])

        empty_pairs = {i:0 for i in list(chain.from_iterable([[k[0] + v, v + k[1]] for k,v in list(map(lambda x: x.strip().split(" -> "), data))]))}

        frequencies = dict(empty_pairs, **letter_freq)


        for i in range(0, 40):
            frequencies = calc_step(frequencies, letter_pairs)


        print(max_minus_min(frequencies, code.strip()))

