from itertools import cycle, product
from dataclasses import dataclass
from functools import lru_cache
import argparse


@dataclass
class player:
    player_id: int
    score: int
    position: int

def deterministic_die():
    die = cycle(range(1, 101))

    pl1 = player(1, 0, 6)
    pl2 = player(2, 0, 9)

    player_1_turn = True
    roll_ctr = 0

    while max(pl1.score, pl2.score) < 1000:
        curr_roll = [next(die), next(die), next(die)]

        cur_player = pl1 if player_1_turn else pl2

        new_pos = (cur_player.position + sum(curr_roll)) % 10

        
        cur_player.position = 10 if new_pos == 0 else new_pos
        cur_player.score += cur_player.position

        player_1_turn = not player_1_turn
        roll_ctr += 3

    print(min(pl1.score, pl2.score)*roll_ctr)

@lru_cache(maxsize=None)
def dirac_round(pl1_score, pl1_pos, pl2_score, pl2_pos, pl1_turn):
    if pl1_score >= 21:
        return [1, 0]
    elif pl2_score >= 21:
        return [0, 1]
    else:
        results = []

        for curr_roll in die_combinations:
            cur_pos = pl1_pos if pl1_turn else pl2_pos

            new_pos = (cur_pos + sum(curr_roll)) % 10

            pos = 10 if new_pos == 0 else new_pos

            if pl1_turn:
                results.append(dirac_round(pl1_score + pos, pos, pl2_score, pl2_pos, False))

            else:
                results.append(dirac_round(pl1_score, pl1_pos, pl2_score + pos, pos, True))


        return [sum([i[0] for i in results]), sum([i[1] for i in results])]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int)
    part = parser.parse_args().part

    if part == 1:
        deterministic_die()

    else:
        die_combinations = list(product([1, 2, 3], repeat=3))
        print(max(dirac_round(0, 6, 0, 9, True)))


