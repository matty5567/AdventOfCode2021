
with open(r"day_1\data.txt") as data:
    sonar_data = [int(i) for i in data.readlines()]

print(len(sonar_data))

count = 0
prev_reading = sonar_data[0]

for reading in sonar_data:
    if reading > prev_reading:
        count += 1
    prev_reading = reading





