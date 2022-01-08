import re
import argparse
import numpy as np
from math import prod


def parse_points(point):
    instr, coords = point.split(" ")
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", coords))
    return ({"on":1, "off":0}[instr], x1, x2, y1, y2, z1, z2)


def part_1(instr):
    cubes = np.zeros((101, 101, 101), dtype=int)

    for setting, x1, x2, y1, y2, z1, z2 in instr:
        for x in range(max(x1, -50), min(x2, 50)+1):
            for y in range(max(y1, -50), min(y2, 50)+1):
                for z in range(max(z1, -50), min(z2, 50)+1):
                    cubes[x+50, y+50, z+50] = setting

    print(np.sum(cubes))


def calc_overlap(a, b):
    max_x1, min_x2 = max(a[1], b[1]), min(a[2], b[2])
    max_y1, min_y2 = max(a[3], b[3]), min(a[4], b[4])
    max_z1, min_z2 = max(a[5], b[5]), min(a[6], b[6])

    return None if any([min_x2 < max_x1, min_y2 < max_y1, min_z2 < max_z1]) else (-b[0], max_x1, min_x2, max_y1, min_y2, max_z1, min_z2)



def calc_volume(sign, x1, x2, y1, y2, z1, z2):
    return sign * (x2-x1+1) * (y2-y1+1) * (z2-z1+1)


def part2(points):
    cubes_on = []
    
    for cuboid in points:
        cuboids = [cuboid] if cuboid[0]==1 else []
        cuboids += [overlap for i in cubes_on if (overlap := calc_overlap(cuboid, i))]
        cubes_on += cuboids

    total = sum([calc_volume(*i) for i in cubes_on])

    print(total)



with open(r'data.txt') as f:
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int)
    part = parser.parse_args().part
    instr = [parse_points(i) for i in f.readlines()]

    if part == 1:
        part_1(instr)

    else:
        part2(instr)



