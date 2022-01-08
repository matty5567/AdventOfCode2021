
chars = {"(":")", "{":"}", "<":">", "[":"]"}
syntax_lookup = {")": 3, "]": 57, "}": 1197, ">": 25137}

with open(r'day_10/data.txt') as f:
    syntax_score = 0
    input_lines = f.readlines()
    
    for line in input_lines:
        buffer = []
        for char in line.strip():
            if char in chars.keys():
                buffer.append(char)
            elif char == chars[buffer[-1]]:
                buffer.pop(-1)
            else:
                syntax_score += syntax_lookup[char]
                break

    print(syntax_score)