# Advent of code day 3 part 1

# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which
# gear needs to be replaced.

# Consider the same engine schematic again:
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
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear
# ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
# because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
#
# What is the sum of all of the gear ratios in your engine schematic?

# variable to hold the full schematic
schematic = []


# function to check if the passed in coordinate is valid
def is_valid_coordinate(line, column):
    if 0 <= line < sch_lines and 0 <= column < sch_size:
        return True
    else:
        return False


# function to check if a line contains a number
# returns the index of the first number or -1 otherwise
def contains_number(line):
    length = len(line)

    for i in range(length):
        if line[i].isdigit():
            return i

    return -1


# function to determine if gear is real
# if the gear is real, this function returns the gear ratio
def is_valid_gear(line, column):
    print(line, column)

    # lists to hold all the characters that are adjacent to the potential gear
    # 4 strings to hold the above, below, left, and right lines
    adjacent_chars_above = adjacent_chars_below = adjacent_chars_right = adjacent_chars_left = ""

    test_line = 0
    test_column = 0

    # check top-left
    test_line = line - 1
    test_column = column - 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_above = schematic[test_line][test_column]

    # check directly above
    test_line = line - 1
    test_column = column
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_above = adjacent_chars_above + (schematic[test_line][test_column])

    # check top-right
    test_line = line - 1
    test_column = column + 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_above = adjacent_chars_above + (schematic[test_line][test_column])

    # check bottom-left
    test_line = line + 1
    test_column = column - 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_below = (schematic[test_line][test_column])

    # check directly below
    test_line = line + 1
    test_column = column
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_below = adjacent_chars_below + (schematic[test_line][test_column])

    # check bottom-right
    test_line = line + 1
    test_column = column + 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_below = adjacent_chars_below + (schematic[test_line][test_column])

    # check directly left
    test_line = line
    test_column = column - 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_left = schematic[test_line][test_column]

    # check directly right
    test_line = line
    test_column = column + 1
    if is_valid_coordinate(test_line, test_column):
        adjacent_chars_right = schematic[test_line][test_column]

    print("Above", adjacent_chars_above)
    print("Left", adjacent_chars_left, "Right", adjacent_chars_right)
    print("Below", adjacent_chars_below)

    # variables to hold the adjacent numbers
    above_num = left_num = right_num = below_num = ""

    # check left for numbers
    if adjacent_chars_left.isdigit():
        test_line = line
        test_column = column - 1

        while (schematic[test_line][test_column]).isdigit():
            left_num = schematic[test_line][test_column] + left_num
            test_column -= 1

            # break out if we hit the edge of the schematic
            if not is_valid_coordinate(test_line, test_column):
                break

        left_num = int(left_num)
        print("left num is", left_num)

    # check right for numbers
    if adjacent_chars_right.isdigit():
        test_line = line
        test_column = column + 1

        # iterate to the last digit
        while (schematic[test_line][test_column]).isdigit():
            right_num = right_num + schematic[test_line][test_column]
            test_column += 1

            # break out if we hit the edge of the schematic
            if not is_valid_coordinate(test_line, test_column):
                break

        print("right num is", right_num)
        right_num = int(right_num)

    # check above for numbers
    above_index = contains_number(adjacent_chars_above)
    if above_index != -1:
        # check column above gear
        test_line = line - 1

        if above_index == 0:
            if column == 0:
                test_column = 0
            else:
                test_column = column - 1
                # find the first digit of the number
                while (schematic[test_line][test_column - 1]).isdigit():
                    test_column -= 1

        elif above_index == 1:
            test_column = column
            # check to see if this is above or top right
            if (schematic[test_line][test_column]) == '.':
                test_column = column + 1

        elif above_index == 2:
            test_column = column + 1

        # iterate to the last digit
        while (schematic[test_line][test_column]).isdigit():
            above_num = above_num + schematic[test_line][test_column]
            test_column += 1

            # break out if we hit the edge of the schematic
            if not is_valid_coordinate(test_line, test_column):
                break

        above_num = int(above_num)
        print("above num is", above_num)

        # check above for numbers
        below_index = contains_number(adjacent_chars_below)
        if below_index != -1:
            # check column below gear
            test_line = line + 1

            if below_index == 0:
                if column == 0:
                    test_column = 0
                else:
                    test_column = column - 1
                    # find the first digit of the number
                    while (schematic[test_line][test_column - 1]).isdigit():
                        test_column -= 1

            elif below_index == 1:
                test_column = column
                # check to see if this is above or top right
                if (schematic[test_line][test_column]) == '.':
                    test_column = column + 1

            elif below_index == 2:
                test_column = column + 1

            # iterate to the last digit
            while (schematic[test_line][test_column]).isdigit():
                below_num = below_num + schematic[test_line][test_column]
                test_column += 1

                # break out if we hit the edge of the schematic
                if not is_valid_coordinate(test_line, test_column):
                    break

            below_num = int(below_num)
            print("below num is", below_num)

    total_adj_nums = 4
    if above_num == "":
        total_adj_nums -= 1
        above_num = 1
    if below_num == "":
        total_adj_nums -= 1
        below_num = 1
    if left_num == "":
        total_adj_nums -= 1
        left_num = 1
    if right_num == "":
        total_adj_nums -= 1
        right_num = 1

    print("total adj nums", total_adj_nums)
    if total_adj_nums == 2:
        ratio = above_num * below_num * left_num * right_num
        print("gear ratio =", ratio)
        return ratio
    else:
        return 0


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

    # iterate through the schematic file to find the gears
    for i in range(sch_lines):
        for j in range(sch_size):
            # if we find a gear
            if schematic[i][j] == '*':
                total += is_valid_gear(i, j)

    print("Part number total =", total)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
