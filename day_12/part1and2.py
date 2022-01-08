from collections import defaultdict, Counter
from itertools import chain

class caveNetwork:
    def __init__(self, data, part):
        self.nodes = defaultdict(list)
        self.part = part

        for a, b in data:
            self.nodes[a].append(b)
            self.nodes[b].append(a)
        

        self.all_paths = list(filter(lambda x:x[-1] == "end", self.find_all_paths(["start"])))
        
        print(len(self.all_paths))

    def path_is_valid(self, path):
        if self.part == 1:
            curr_node = path[-1]
            return not(curr_node.islower() and curr_node in path[:-1])
        else:
            nodes_visited = list(Counter(filter(lambda x: x.islower(), path)).values())
            return list(nodes_visited).count(2) <= 1 and not list(filter(lambda x: x>2, nodes_visited)) and path.count("start")==1


    def find_all_paths(self, path):
        curr_node = path[-1]

        if curr_node=="end":
            return [path]        

        return list(chain.from_iterable([self.find_all_paths(path + [child]) for child in self.nodes[curr_node] if self.path_is_valid(path + [child])]))

    

with open(r'day_12/data.txt') as f:
    data = list(map(lambda x: x.strip().split("-"), f.readlines()))
    caves = caveNetwork(data, 2)