with open(r"day_1\data.txt") as data:
    sonar_data = [int(i) for i in data.readlines()]



count = 0
prev_sum = sum(sonar_data[0:3])

print(prev_sum)

for i in range(len(sonar_data) - 2):
    cur_sum = sum(sonar_data[i:i+3])
    if cur_sum > prev_sum:
        count += 1
    prev_sum = cur_sum

print(count)