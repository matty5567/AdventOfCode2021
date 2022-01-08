import numpy as np

chars = {"(":")", "{":"}", "<":">", "[":"]"}
syntax_lookup = {")": 1, "]": 2, "}": 3, ">": 4}


def calc_score(line):
    sum = 0
    for char in line:
        sum *=5
        sum += syntax_lookup[char]
    return sum

with open(r'day_10/data.txt') as f:
    syntax_score = 0
    input_lines = f.readlines()
    line_scores = []
    
    for line in input_lines:
        corrupt = False
        buffer = []
        for char in line.strip():
            if char in chars.keys():
                buffer.append(char)
            elif char == chars[buffer[-1]]:
                buffer.pop(-1)
            else:
                corrupt = True
                break

        if buffer and not corrupt:
            completion_string = [chars[i] for i in buffer][::-1]
            line_scores.append(calc_score(completion_string))

    print(np.median(line_scores))