# Advent of code day 3 part 1
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers
# and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part
# number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58
# (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
# schematic?

# variable to hold the full schematic
schematic = []


# function to check if the passed in coordinate is valid
def is_valid_coordinate(line, column):
    if 0 <= line < sch_lines and 0 <= column < sch_size:
        return True
    else:
        return False


# function to determine if the current number is adjacent to any special characters
# The arguments passed in are the size of the number and the coordinates of its first digit in the schematic
# The function returns True if the number is a real part number, and returns False otherwise
def is_adjacent(size, line, column):
    print(size, line, column)

    # list to hold all the characters that are adjacent to the number
    adjacent_chars = []

    for i in range(size):
        # variables to hold the coordinates currently being tested
        test_line = 0
        test_column = 0

        # check above and below for each character
        # check directly above
        test_line = line - 1
        test_column = column
        if is_valid_coordinate(test_line, test_column):
            adjacent_chars.append(schematic[test_line][test_column])

        # case 4:  # check directly below
        test_line = line + 1
        test_column = column
        if is_valid_coordinate(test_line, test_column):
            adjacent_chars.append(schematic[test_line][test_column])

        # if we're at the first digit check the surrounding coordinates on the left
        if i == 0:
            # check top-left
            test_line = line - 1
            test_column = column - 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

            # check directly left
            test_line = line
            test_column = column - 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

            # check bottom-left
            test_line = line + 1
            test_column = column - 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

        # if we're at the last digit, check the surrounding coordinates on the right
        if i == size - 1:
            # check top-right
            test_line = line - 1
            test_column = column + 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

            # check directly right
            test_line = line
            test_column = column + 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

            # check bottom-right
            test_line = line + 1
            test_column = column + 1
            if is_valid_coordinate(test_line, test_column):
                adjacent_chars.append(schematic[test_line][test_column])

        # update column to move to next digit
        column += 1

    # iterate through the list and find if any of the adjacent characters are special
    for i in range(len(adjacent_chars)):
        if adjacent_chars[i] != '.':
            return True

    return False


def main():
    # variables to hold the number of lines in the schematic, as well as the size of each line
    global sch_lines
    global sch_size

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file
    current = in_file.readline()
    # size - 1 since we'll be removing the last char from each line
    sch_size = len(current) - 1
    sch_lines = 0

    # final part number total
    total = 0

    # loop to copy the file into the schematic[] list
    while current:
        sch_lines += 1

        # add current line to schematic after removing the \n at the end
        schematic.append(current[0:sch_size])

        # read the next line from the file
        current = in_file.readline()

    # close file since we've copied the schematic into memory
    in_file.close()

    # iterate through the schematic file to find all part numbers and determine if they're adjacent to a special char
    for i in range(sch_lines):
        j = 0
        while j < sch_size - 1:
            # variable to store the current number
            curr_part = ""

            # find the next number in the schematic
            if schematic[i][j].isdigit():
                curr_part = schematic[i][j]

                # iterate to the end of the number
                j += 1
                while schematic[i][j].isdigit():
                    curr_part = curr_part + schematic[i][j]
                    j += 1

                    # break out of the loop if we're at the end of the current line
                    if j == sch_size:
                        break

            # if we've found a number, find if it's adjacent
            if curr_part:
                curr_size = len(curr_part)
                if is_adjacent(curr_size, i, j - curr_size):
                    total += int(curr_part)

            j += 1

    print("Part number total =", total)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
