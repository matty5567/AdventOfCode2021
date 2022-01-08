from itertools import chain
from collections import Counter

def decode_input(input):
    coded_leters = ["a", "b", "c", "d", "e", "f", "g"]
    coded_dict = {i:None for i in coded_leters}

    # a is in all apart from ones with length 1 and 4
    letters = [set(i for i in code) for code in filter(lambda x: len(x) not in [2, 4], input)]
    coded_dict["a"] = "".join(set.intersection(*letters))

    
    letter_freq = Counter(list(chain(*input)))

    # e appears 4 times
    coded_dict["e"] = list(letter_freq.keys())[list(letter_freq.values()).index(4)]

    # b appears 6 times
    coded_dict["b"] = list(letter_freq.keys())[list(letter_freq.values()).index(6)]


    # two digits must be 1 (c, f)
    c_and_f = [i for i in list(filter(lambda x: len(x)==2, input))[0]]

    # c appears 8 times
    coded_dict["c"] = next(filter(lambda x:letter_freq[x]==8, c_and_f))
    
    # f appears 9 times
    coded_dict["f"] = next(filter(lambda x:letter_freq[x]==9, c_and_f))

    

    # 4 digits must be 4 (b, c, d, f)
    coded_dict["d"] = next(filter(lambda x:x not in list(coded_dict.values()), [i for i in list(filter(lambda x: len(x)==4, input))[0]]))
    
    # g is last remaining letter
    coded_dict["g"] = "".join(set(coded_dict.keys()) - set(coded_dict.values()))

    return {v:k for k, v in coded_dict.items()}


digits = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

with open(r'day_8\data.txt') as f:
    lines = [i.split("|") for i in f.readlines()]
    sum = 0
    for line in lines:
        input = line[0].strip().split(" ")
        reading = line[1].strip().split(" ")
        decoding_dict = decode_input(input)
        
        sum += int("".join(list(map(lambda x: digits["".join(sorted([decoding_dict[i] for i in x]))], reading))))
        
    print(sum)