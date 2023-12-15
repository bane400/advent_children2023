# Advent of code day 10
# Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to
# tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the
# surface pipes you can see (your puzzle input).
#
# The pipes are arranged in a two-dimensional grid of tiles:
#
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the
# pipe has.
# Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large,
# continuous loop.
#
# For example, here is a square loop of pipe:
#
# .....
# .F-7.
# .|.|.
# .L-J.
# .....
# If the animal had entered this loop in the northwest corner, the sketch would instead look like this:
#
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect
# to it.
#
# Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:
#
# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
# In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes
# those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two
# neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to
# those two pipes).
#
# Here is a sketch that contains a slightly more complex main loop:
#
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
#
# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting
# position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you
# need to find the tile that would take the longest number of steps along the loop to reach from the starting point -
# regardless of which way around the loop the animal went.
#
# In the first example with the square loop:
#
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# You can count the distance each tile in the loop is from the starting point like this:
#
# .....
# .012.
# .1.3.
# .234.
# .....
# In this example, the farthest point from the start is 4 steps away.
#
# Here's the more complex loop again:
#
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# Here are the distances for each tile on that loop:
#
# ..45.
# .236.
# 01.78
# 14567
# 23...
# Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position
# to the point farthest from the starting position?

pipe_map = []
sch_lines = 0
sch_size = 0


# function to check if the passed in coordinate is valid
# valid means within the bounds of the map and not a number
def is_valid_coordinate(line, column):
    if 0 <= line < sch_lines and 0 <= column < sch_size and not pipe_map[line][column].isdigit():
        return True
    else:
        return False


def parse_file():
    # let python know pipe_map is global
    global pipe_map

    # open file to parse
    in_file = open("../firsttest.txt", "rt")

    # read the 2nd line in the file and remove the \n
    current = in_file.readline()[0:-1]

    # iterate through file
    while current:
        line = []
        for i in range(len(current)):
            line.append(current[i])

        pipe_map.append(line)

        # read in next line
        current = in_file.readline()[0:-1]






# check if there is a connecting pipe above the given coordinate
# function returns True if there is a valid pipe
def check_above(line, column):
    n_x = line - 1
    n_y = column
    if is_valid_coordinate(n_x, n_y):
        # check if the pipe actually touches the starting coordinate
        if pipe_map[n_x][n_y] == '|' or pipe_map[n_x][n_y] == 'T' or pipe_map[n_x][n_y] == 'F':
            return True

    return False


# check if there is a connecting pipe below the given coordinate
# function returns True if there is a valid pipe
def check_below(line, column):
    n_x = line + 1
    n_y = column
    if is_valid_coordinate(n_x, n_y):
        # check if the pipe actually touches the starting coordinate
        if pipe_map[n_x][n_y] == '|' or pipe_map[n_x][n_y] == 'L' or pipe_map[n_x][n_y] == 'J':
            return True

    return False


# check if there is a connecting pipe east of the given coordinate
# function returns True if there is a valid pipe
def check_east(line, column):
    # check east
    n_x = line
    n_y = column + 1
    if is_valid_coordinate(n_x, n_y):
        # check if the pipe actually touches the starting coordinate
        if pipe_map[n_x][n_y] == '-' or pipe_map[n_x][n_y] == 'J' or pipe_map[n_x][n_y] == 'T':
            return True

    return False


# check if there is a connecting pipe west of the given coordinate
# function returns True if there is a valid pipe
def check_west(line, column):
    n_x = line
    n_y = column - 1
    if is_valid_coordinate(n_x, n_y):
        # check if the pipe actually touches the starting coordinate
        if pipe_map[n_x][n_y] == '-' or pipe_map[n_x][n_y] == 'L' or pipe_map[n_x][n_y] == 'F':
            return True

    return False


# function to find the next connecting pipes from a node
# returns a list of coordinates to go to and fills in the map with numbers
def find_next(coord, step):
    next_coords = []

    # iterate through the list of next coordinates
    for i in range(len(coord)):
        tile = pipe_map[coord[i][0]][coord[i][1]]
        print(tile)

        # update the map
        pipe_map[coord[i][0]][coord[i][1]] = step

        match tile:
            # starting position
            case 'S':
                break
            # vertical pipe
            case '|':
                # check above
                n_x = coord[i][0] - 1
                n_y = coord[i][1]
                if is_valid_coordinate(n_x, n_y):
                    # check if the pipe actually touches the starting coordinate
                    if pipe_map[n_x][n_y] == '|' or pipe_map[n_x][n_y] == 'T' or pipe_map[n_x][n_y] == 'F':
                        next_coords.append(tuple([n_x, n_y]))

                # check below
                n_x = coord[i][0] + 1
                n_y = coord[i][1]
                if is_valid_coordinate(n_x, n_y):
                    # check if the pipe actually touches the starting coordinate
                    if pipe_map[n_x][n_y] == '|' or pipe_map[n_x][n_y] == 'L' or pipe_map[n_x][n_y] == 'J':
                        next_coords.append(tuple([n_x, n_y]))

            # # horizontal pipe
            # case '-':
            #
            # # north-east pipe
            # case 'L':
            #
            # # north-west pipe
            # case 'J':
            #
            # # south-west pipe
            # case 'T':
            #
            # # south-east pipe
            # case 'F':

    return next_coords


def main():
    # variables to hold the number of lines in the schematic, as well as the size of each line
    global sch_lines
    global sch_size

    # variable to hold the max distance
    dist = 0

    # variable to hold starting position
    # making this a list makes things easier
    start = []

    # parse input to 2d list
    parse_file()

    sch_lines = len(pipe_map)
    sch_size = len(pipe_map[0])

    # find the start location and repalce all 7's with T's
    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[i])):
            if pipe_map[i][j] == 'S':
                start.append(tuple((i, j)))
            if pipe_map[i][j] == '7':
                pipe_map[i][j] = 'T'

    print(start)
    print(sch_lines)
    print(sch_size)

    # find all the points connecting to the start
    i = 0
    next_points = find_next(start, str(i))

    print(next_points)
    print(pipe_map)

    # find all the next pipes until there aren't any left
    while next_points:
        i += 1
        next_points = find_next(next_points, str(i))
        print(next_points)
        print(pipe_map)

    print("Farthest distance is", dist)


if __name__ == "__main__":
    main()
