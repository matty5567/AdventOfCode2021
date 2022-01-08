
    

from typing import DefaultDict
from itertools import cycle

class school():
    def __init__(self, list_ages):
        self.school = dict(zip(range(9), cycle([0])))
        for i in list_ages:
            self.school[i] += 1
        print(self.school)

    def age_school_by_one_day(self):
        new_fish = self.school[0]
        
        for i in range(0, 8):
            self.school[i] = self.school[i+1]
        
        self.school[8] = new_fish
        self.school[6] += new_fish

    
    def __str__(self):
        return str(sum(self.school.values()))

    def simulate(self, num_days):
        for i in range(num_days):
            self.age_school_by_one_day()



with open(r'day_6\data.txt') as f:
        
    population =  school([int(i) for i in f.read().split(',')])
    population.simulate(256)
    print(population)
