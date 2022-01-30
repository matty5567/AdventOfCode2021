
bad_states   = set()
z_div_lookup = [1 , 1 , 1 , 1 , 1 , 26,  1,  26,  26,  1,  26, 26, 26, 26]
x_add_lookup = [10, 12, 13, 11, 14, -2, 11, -15, -10, 10, -10, -4, -1, -1]
y_add_lookup = [0 , 1 , 1 , 4 ,  9,  1, 10,   6,   4,  6,   3,  9, 15,  5]

def solve(digits, depth, prev_z, num):

    if (depth, prev_z) in bad_states or depth==14:
        return None

    if depth == 0:
        print(num)

    # Shift along one base 10
    num *= 10

    for i in digits:

        z = prev_z
        w = i
        x = z
        x %= 26
        z /= z_div_lookup[depth]
        x += x_add_lookup[depth]
        x = int(x == w)
        x = int(x == 0)
        y = 25
        y *= x
        y += 1
        z *= y
        y = w
        y += y_add_lookup[depth]
        y *= x
        z += y

        if depth == 13 and z == 0:
            return num + i

        elif (ret := solve(digits, depth + 1, z, num + i)):
            return ret

    bad_states.add((depth, prev_z))
    return None


def part2():
    digits = range(9, -1, -1)
    print(solve(digits, 0, 0, 0))

def part1():
    digits = range(0, 10, 1)
    print(solve(digits, 0, 0, 0))


if __name__=="__main__":
    part2()
