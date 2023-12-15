# Advent of code day 14
# In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets
# you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-
# shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle
# input). For example:
#
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# Start by tilting the lever so all of the rocks will slide north as far as they will go:
#
# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....
# You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't
# collapse, you should calculate the total load on the north support beams.
#
# The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge
# of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of
# load caused by each rock in each row is as follows:
#
# OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1
# The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.
#
# Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support
# beams?


# global to hold the rock pattern
rocks = []


def parse_file():
    # let python know rocks is global
    global rocks

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the 2nd line in the file
    current = in_file.readline()

    while current:
        next_pattern = [i for i in current.strip()]

        rocks.append(next_pattern)
        current = in_file.readline()

    # close file once the function completes
    in_file.close()


# function to move each rock as far north as possible
def move_up():
    # skip the first row since they're as far north as possible already
    for i in range(1, len(rocks), 1):
        for j in range(len(rocks[i])):
            # if we find a movable rock, find the northmost spot it can go
            if rocks[i][j] == 'O':
                index = i
                while index > 0:
                    if rocks[index - 1][j] == 'O' or rocks[index - 1][j] == '#':
                        break
                    index -= 1

                # fill in the found location with a rock and remove the rock at the previous location, if it needs to be
                # moved
                if index != i:
                    rocks[index][j] = 'O'
                    rocks[i][j] = '.'


def pattern_printer(pattern):
    for i in range(len(pattern)):
        print(pattern[i], i + 1)


def main():
    # variable to hold the final answer
    load = 0

    # parse input to a list of patterns
    parse_file()

    # move all the rocks north
    move_up()

    for i in range(len(rocks)):
        num_rocks = 0
        for j in range(len(rocks[i])):
            if rocks[i][j] == 'O':
                num_rocks += 1

        load += num_rocks * (len(rocks) - i)

    pattern_printer(rocks)

    print("Total load on beams", load)


if __name__ == "__main__":
    main()
