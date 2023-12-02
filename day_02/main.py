# Advent of code day 1
# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random
# cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
#
# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID
# number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed
# from the bag (like 3 red, 5 green, 4 blue).
#
# For example, the record of a few games might look like this:
#
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and
# 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#
# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green
# cubes, and 14 blue cubes?
#
# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
# However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly,
# game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the
# games that would have been possible, you get 8.
#
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and
# 14 blue cubes. What is the sum of the IDs of those games?


# this function takes a set and returns a tuple of the red, green, and blue values (in that order)
def cube_amounts(line):
    # variables to hold the cube amounts of each color
    red = green = blue = 0

    # the length of the passed in string
    size = len(line)

    # list to store the number of each color
    amounts = []
    start = 0
    for i in range(size):
        # check if we've reached a colon
        if line[i] == ',':
            # add the sub-string to amounts
            amounts.append(line[start:i])

            # set the new starting index of the next sub-string
            start = i + 1

        # check if we're at the end of the string
        elif i == size - 1:
            amounts.append(line[start:size])

    # iterate through amounts to extract r/g/b value
    for i in range(len(amounts)):
        # store the current string we're working with
        current = amounts[i]

        # update size to the current string
        size = len(current)

        # iterate through string to find value and color
        for j in range(1, size):
            if current[j] == ' ':
                color = current[j + 1:size]
                match color:
                    case "red":
                        red = int(current[0:j])
                    case "blue":
                        blue = int(current[0:j])
                    case "green":
                        green = int(current[0:j])

    return red, green, blue


# function to remove the part of the line that says "Game x:"
def format_line(line):
    # the length of the passed in string
    size = len(line)

    for i in range(size):
        if line[i] == ':':
            return line[i + 1:size]


# function to check if a current game is valid
# this function will return the game ID if the game is valid, or 0 otherwise
def is_valid_game_part1(line):
    # variable to store the functions return value
    is_valid = True

    # list to store the sets of cubes that are pulled
    sets = []

    # remove the part of the line that says "Game x:"
    formatted_line = format_line(line)

    # set size to that of the formatted line
    size = len(formatted_line)

    # divide the line into the sets of cubes
    # store where the current sub-string starts
    start = 0
    for i in range(size):
        # check if we've reached a semicolon or the end of the string
        if formatted_line[i] == ';' or i == size - 1:
            # add the sub-string to sets
            # start + 1 is to remove the space at the beginning
            sets.append(formatted_line[start + 1:i])

            # set the new starting index of the next sub-string
            start = i + 1

    # iterate through the list of sets to see if they're valid
    for i in range(len(sets)):
        rgb_tuple = cube_amounts(sets[i])

        # check if any of the returned values violate the cube amounts
        # 12 red cubes, 13 green cubes, and 14 blue cubes
        if rgb_tuple[0] > 12 or rgb_tuple[1] > 13 or rgb_tuple[2] > 14:
            is_valid = False

        # if the current set isn't valid, then we don't need to check the rest of the sets
        if not is_valid:
            break

    return is_valid


# PART TWO
# As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of
# cubes of each color that could have been in the bag to make the game possible?
# This function returns the power value of the current line
def is_valid_game_part2(line):
    # variable to store the max number of cubes for each color
    red_max = blue_max = green_max = 0

    # list to store the sets of cubes that are pulled
    sets = []

    # remove the part of the line that says "Game x:"
    formatted_line = format_line(line)

    # set size to that of the formatted line
    size = len(formatted_line)

    # divide the line into the sets of cubes
    # store where the current sub-string starts
    start = 0
    for i in range(size):
        # check if we've reached a semicolon or the end of the string
        if formatted_line[i] == ';' or i == size - 1:
            # add the sub-string to sets
            # start + 1 is to remove the space at the beginning
            sets.append(formatted_line[start + 1:i])

            # set the new starting index of the next sub-string
            start = i + 1

    # iterate through the sets to get the list of tuples
    rgb_tuples = []
    for i in range(len(sets)):
        rgb_tuples.append(cube_amounts(sets[i]))

    # iterate through each color to find the largest value in the list
    for i in range(3):
        # temporary space to store current max value of the color
        temp = 0

        for j in range(len(rgb_tuples)):
            if rgb_tuples[j][i] > temp:
                temp = rgb_tuples[j][i]

        # set the temp value to the appropriate value
        match i:
            case 0:  # Red color
                red_max = temp
            case 1:  # Green color
                green_max = temp
            case 2:  # Blue color
                blue_max = temp

    return red_max * blue_max * green_max


def main():
    in_file = open("finaltest.txt", "rt")

    # sum of valid game ID
    total = 0

    # read the first line in the file
    current = in_file.readline()
    lines = 0

    # loop to iterate to the end of the file line by line
    while current:
        lines += 1

        # Get the current line's power value and add it to the total
        total += is_valid_game_part2(current)

        # read the next line from the file
        current = in_file.readline()

    print("Sum of valid IDs =", total)

    # close file once the program completes
    in_file.close()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
