# Advent of code day 11
# The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The
# image includes empty space (.) and galaxies (#). For example:
#
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies.
# However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the
# observatory.
#
# Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or
# columns that contain no galaxies should all actually be twice as big.
#
# In the above example, three columns and two rows contain no galaxies:
#
#    v  v  v
#  ...#......
#  .......#..
#  #.........
# >..........<
#  ......#...
#  .#........
#  .........#
# >..........<
#  .......#..
#  #...#.....
#    ^  ^  ^
# These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:
#
# ....#........
# .........#...
# #............
# .............
# .............
# ........#....
# .#...........
# ............#
# .............
# .............
# .........#...
# #....#.......
# Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to
# assign every galaxy a unique number:
#
# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# ............6
# .............
# .............
# .........7...
# 8....9.......
# In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each
# pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one
# . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)
#
# For example, here is one of the shortest paths between galaxies 5 and 9:
#
# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# .##.........6
# ..##.........
# ...##........
# ....##...7...
# 8....9.......
# This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations
# marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:
#
# Between galaxy 1 and galaxy 7: 15
# Between galaxy 3 and galaxy 6: 17
# Between galaxy 8 and galaxy 9: 5
# In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.
#
# Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of
# these lengths?


# global to hold the image of the galaxies
galaxies = []
galaxy_coords = []
num_galaxies = 0
extra_rows = []
extra_cols = []


def parse_file():
    # let python know pipe_map is global
    global galaxies

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the 2nd line in the file and remove the \n
    current = in_file.readline()[0:-1]

    while current:
        galaxies.append(list(current))

        # read in next line
        current = in_file.readline()[0:-1]

    # close file once the program completes
    in_file.close()


# replaces all '#' in the map with ordered numbers and save the coordinates
def count_galaxies():
    # tell python that these are globals
    global num_galaxies
    global galaxy_coords

    count = 0
    for i in range(len(galaxies)):
        for j in range(len(galaxies[i])):
            if galaxies[i][j] == '#':
                count += 1
                galaxies[i][j] = count
                galaxy_coords.append(tuple((i, j)))

    num_galaxies = count


# function to calculate the number of rows/columns to expand the universe by
def expand():
    # tell python that these are globals
    global extra_rows
    global extra_cols

    # iterate through the rows
    for i in range(len(galaxies)):
        # check if all elements in the row are the same
        curr = galaxies[i][0]
        result = True
        for j in range(len(galaxies[i])):
            if curr != galaxies[i][j]:
                result = False
                break

        # if all the elements are the same add a 1 to the list, 0 otherwise
        if result:
            extra_rows.append(1)
        else:
            extra_rows.append(0)

    # iterate through the columns
    for i in range(len(galaxies[0])):
        # check if all elements in the row are the same
        curr = galaxies[0][i]
        result = True
        for j in range(len(galaxies)):
            if curr != galaxies[j][i]:
                result = False
                break

        # if all the elements are the same add a 1 to the list, 0 otherwise
        if result:
            extra_cols.append(1)
        else:
            extra_cols.append(0)


# function to calculate the distance between two nodes
# returns the distance
def distance(coord1, coord2):
    # sort the x and y coordinates
    x = sorted([coord1[0], coord2[0]])
    y = sorted([coord1[1], coord2[1]])

    # count the number of expansion rows between the given rows
    add_rows = 0
    for i in range(x[0], x[1], 1):
        if extra_rows[i]:
            add_rows += 1

    # do the same for the columns
    add_cols = 0
    for i in range(y[0], y[1], 1):
        if extra_cols[i]:
            add_cols += 1

    # sum up distances
    x_dist = x[1] - x[0] + add_rows
    y_dist = y[1] - y[0] + add_cols
    dist = x_dist + y_dist

    return dist


def main():
    # variable to hold the total distance between galaxies
    dist = 0

    # parse input to 2d list then extract the relevant galaxy information
    parse_file()
    count_galaxies()

    # calculate the number of extra rows/columns to add
    expand()

    # iterate through the list of galaxies and calculate distance
    for i in range(num_galaxies):
        for j in range(i + 1, num_galaxies, 1):
            dist += distance(galaxy_coords[i], galaxy_coords[j])

    print("Sum of distance is", dist)


if __name__ == "__main__":
    main()
