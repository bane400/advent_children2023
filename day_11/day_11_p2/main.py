# Advent of code day 11 part 2
# The galaxies are much older (and thus much farther apart) than the researcher initially estimated.
#
# Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each
# empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty
# columns.
#
# (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between
# every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the
# shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond
# these values.)
#
# Starting with the same initial image, expand the universe according to these new rules, then find the length of the
# shortest path between every pair of galaxies. What is the sum of these lengths?


# global to hold the image of the galaxies and the auxiliary info
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
    # additional rows/columns times 999999 to account found new expansion rules
    x_dist = x[1] - x[0] + (add_rows * 999999)
    y_dist = y[1] - y[0] + (add_cols * 999999)
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
