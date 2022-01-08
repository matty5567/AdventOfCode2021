from math import sqrt
from itertools import permutations
import numpy as np
from scipy.spatial.transform import Rotation

def cart_dist(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)

def calc_distances(points):
    distances = {}
    for i, j in permutations(enumerate(points), 2):
        distances[round(cart_dist(i[1], j[1]), 4)] = (i[0], j[0])
    return distances
    
def calc_orientations(points):
    for rot in Rotation.create_group("O").as_matrix():
        yield np.matmul(rot, points).astype(int), rot

def calc_largest_mhattan_dist(locs):
    largest_dist = 0
    for i, j in permutations(locs, 2):
        if (dist := abs(i[0]-j[0]) + abs(i[1]-j[1]) + abs(i[2]-j[2])) > largest_dist:
            largest_dist = dist
    return largest_dist

def find_matching_scanners(scanner_data, beacon_map):
    unused_scanners = []
    dist2 = calc_distances(beacon_map)

    for points in scanner_data:

        dist1 = calc_distances(points)
        
        match_dist = list(set(dist1.keys()).intersection(set(dist2.keys())))

        if len(match_dist) >= 66:
            match_point = [points[dist1[match_dist[0]][0]], points[dist1[match_dist[0]][1]], beacon_map[dist2[match_dist[0]][0]], beacon_map[dist2[match_dist[0]][1]]]


            targ_orient = [match_point[2][i] - match_point[3][i] for i in range(3)]

            for i in calc_orientations(np.array(match_point[0:2]).transpose()):

                point_1 = [j[0] for j in i[0]]
                point_2 = [j[1] for j in i[0]]
                distance = [a-b for a, b in zip(point_1, point_2)]

                if distance == targ_orient:
                    disp = [b-a for a, b in zip(point_1, match_point[2])]
                    break
                    
                elif [-i for i in distance] == targ_orient:

                    disp = [b-a for a, b in zip(point_1, match_point[3])]
                    break


            rot_points = zip(*np.matmul(i[1], np.array(points).transpose()).astype(int))

            adj_points = [[a+b for a, b in zip(i, disp)] for i in rot_points]

            beacon_map += adj_points

            scanner_locations.append(disp)

        else:
            unused_scanners.append(points)


    return unused_scanners, beacon_map


if __name__ == "__main__":

    with open('data.txt') as f:
        data = list(map(lambda x: [list(map(int, i.split(','))) for i in x.split('\n')[1:]], f.read().strip().split('\n\n')))
        
        beacon_map = data[0]
        scanner_locations = [[0, 0, 0]]
        scanner_data = data[1:]

        while scanner_data:

            scanner_data, beacon_map = find_matching_scanners(scanner_data, beacon_map)

        

        print(calc_largest_mhattan_dist(scanner_locations))










