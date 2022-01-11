import re
import heapq
from dataclasses import dataclass

@dataclass
class Position:
    _map: str
    cost: int
    f_score = None
    parent = None
    

    def __gt__(self, other):
        return self.f_score > other.f_score
    
    def __lt__(self, other):
        return self.f_score < other.f_score

class Hotel():
    def __init__(self):
        self._map   = "  BDDC ABCA DABB CCAD  "
        
        self.target_rooms = {key: [i+2+idx*5 for i in range(4)] for idx, key in enumerate(["A", "B", "C", "D"])}

        self.room_idxs = {5-j+5*k for k in range(4) for j in range(4)}

        self.corr_idxs = {i for i, _ in enumerate(self._map) if i<2 or i>20 or ((i-1)%5==0)}


        self.move_cost = {"A":1, "B":10, "C":100, "D":1000}
        self.target_map = "  AAAA BBBB CCCC DDDD  "

        self.A_star(self._map)


    def print_map(self, _map):
        print("#" * 13)
        print("#" + _map[:2] + " " + " ".join([_map[i] for i in self.corr_idxs if 2<i<21]) + " " + _map[-2:] + "#")
        for j in range(4):
            print("###" + "#".join([_map[room[3-j]] for room in self.target_rooms.values()]) + "###")
        print("#" * 13)

    def piece_in_way(self, _map, start, end, piece):
        ret = False
        cost = 0


        # check corridor
        # print(end, start, [(6+j)+6*k for k in range(3) for j in range(2)]+[1, 2, 25, 26])
        for i in set(range(end, start, -1 if end > start else 1))&set(self.corr_idxs):
            
            cost += 2 if 1<i<21 or (start not in [0, 22] and i in [1, 21]) else 1 
            if _map[i] != " ":
                ret = True
        
        # check room
        for room in self.target_rooms.values():
            if start in room and end in room:
                ret = True

            for i in [start, end]:
                if i in room:
                    pos = room.index(i)
                    if i==end:
                        cost+=5-pos
                    if i==start:
                        cost += 3-pos

                    for j in room[pos + (1 if start else 0):]:
                        
                        if _map[j] != " ":
                            ret = True

                    if i==end and [j for j in room[:pos] if _map[j] != piece]:
                        ret = True

        return ret, cost*self.move_cost[piece]
    
    def calc_state_options(self, _map, prev_cost):
        spaces = {i.start() for i in re.finditer(" ", _map)}
        
        cor_spaces = spaces & self.corr_idxs
        room_spaces = spaces & self.room_idxs

        piece_idxs = {i.start() for i in re.finditer(r"\w", _map)}

        states = []

        for start in piece_idxs:
            piece = _map[start]
            
            free_spaces = (set(self.target_rooms[piece])&room_spaces).union(cor_spaces if start in self.room_idxs else {})
            for end in free_spaces:
                invalid, cost = self.piece_in_way(_map, start, end, piece)
                if not invalid:
                    if end > start:
                        new_state = _map[:start] + " " + _map[start + 1: end] + piece + _map[end+1:]
                    else:
                        new_state = _map[:end] + piece + _map[end + 1: start] + " " + _map[start+1:]
                    states.append(Position(new_state, prev_cost+cost))
        return states


    def calc_heuristic_dist(self, _map):
        _sum = 0
        for piece, room in self.target_rooms.items():
            for ctr, i in enumerate(room):
                _sum += 0 if _map[i] == piece else (4-ctr)*1

        return _sum

    
    def A_star(self, _map):
        cur_pos  = Position(_map, 0)
        options = []
        closed = []
        seen = {}

        while cur_pos._map != self.target_map:
            closed.append(cur_pos._map)

            for pos in self.calc_state_options(cur_pos._map, cur_pos.cost):
                if pos._map in closed:
                    continue

                dist_to_end = self.calc_heuristic_dist(pos._map)

                if pos.cost < seen.get(pos._map, 1<<32):
                    pos.parent = cur_pos
                    pos.f_score = dist_to_end+pos.cost
                    heapq.heappush(options, pos)
                    seen[pos._map] = pos.cost

            cur_pos = heapq.heappop(options)

        while cur_pos._map != self._map:
            self.print_map(cur_pos._map)
            print(cur_pos.cost)
            print("---------------")
            cur_pos = cur_pos.parent



hotel = Hotel()
