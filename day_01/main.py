# Advent of code day 1
# The newly-improved calibration document consists of lines of text; each line originally contained a specific
# calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining
# the first digit and the last digit (in that order) to form a single two-digit number.
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these lines are 12, 38, 15, and 77. Adding these together produces 142.

# function that takes a line and calculates the calibration value from it
# This function returns the cal val of the line passed in
def cal_val_recovery_v1(line):
    # variables to hold the first and last cal vals from the string
    first = last = 0

    # the length of the passed in string
    size = len(line)

    # iterate through string and find the first cal val
    for i in range(size):
        # print(line[i])
        if line[i].isdigit():
            first = line[i]
            break

    # iterate through string and find the last cal val
    for i in range(size - 1, -1, -1):
        # print(line[i])
        if line[i].isdigit():
            last = line[i]
            break

    # The calibration value is first concatted with last
    cal_val = first + last
    print("The lines cal val is", cal_val, "\n")

    # cast to int and return
    return int(cal_val)

# PART TWO
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two,
# three, four, five, six, seven, eight, and nine also count as valid "digits".


# Function to subdivide the array into all possible strings of lengths 3, 4, and 5
# for example two1nine becomes:
# ['two', 'two1', 'two1n', 'wo1', 'wo1n', 'wo1ni', 'o1n', 'o1ni', 'o1nin', '1ni','1nin', '1nine', 'nin', 'nine', 'ine']
# this function should also keep the arrays in the right order for searching
def str_divide(line):
    # the length of the passed in string
    size = len(line)

    # array to hold the sub_strings created
    sub_strings = []

    for i in range(0, size):
        for j in range(3, 6):
            # break the loop if we're outside the string
            if i >= size - j:
                break
            # extract substring and it's original index
            sub_strings.append((line[i:i + j], i))

    return sub_strings


# function to determine if the passed in line is one of the digits we're looking for
# The digits are one, two, three, four, five, six, seven, eight, and nine
def digit_compare(line):
    match line:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return 0


# function that takes a line and calculates the calibration value from it, based on the new rules
# This function returns the cal val of the line passed in
def cal_val_recovery_v2(line):
    # variables to hold the first and last numerical cal vals from the string
    first = first_index = last = last_index = 0

    # variables to hold the first and last string cal vals from the string
    first_str = first_str_index = last_str = last_str_index = 0

    # variables to hold the final first/last values
    final_first = final_last = 0

    # the length of the passed in string
    size = len(line)

    # iterate through string and find the numerical first cal val
    for first_index in range(size):
        if line[first_index].isdigit():
            first = int(line[first_index])
            break

    # iterate through string and find the numerical last cal val
    for last_index in range(size - 1, -1, -1):
        # print(line[i])
        if line[last_index].isdigit():
            last = int(line[last_index])
            break

    # get all the substrings in this line
    sub_strings = str_divide(line)

    # update size to be the length of the substring array
    size = len(sub_strings)

    # iterate through the substrings to check if there are any matches for the digits
    # start with first value
    for i in range(size):
        value = digit_compare(sub_strings[i][0])
        if value != 0:
            first_str = value
            first_str_index = sub_strings[i][1]
            break

    # now find the last value
    for i in range(size - 1, -1, -1):
        value = digit_compare(sub_strings[i][0])
        if value != 0:
            last_str = value
            last_str_index = sub_strings[i][1]
            break

    # if a number was not found or
    # if the numerical index is greater than the strings, that means the string is the first value
    if (first == 0 or first_index > first_str_index) and first_str != 0:
        final_first = first_str
    else:
        final_first = first

    # Almost the same for the first value, but we need use less than instead of greater, since were going backwards
    # through the string
    if (last == 0 or last_index < last_str_index) and first_str != 0:
        final_last = last_str
    else:
        final_last = last

    cal_val = 10 * final_first + final_last
    return cal_val


def main():
    # open file to parse
    in_file = open("finaltest.txt", "rt")

    # final calibration value
    total = 0

    # read the first line in the file
    current = in_file.readline()
    lines = 0

    # loop to iterate to the end of the file line by line
    while current:
        lines += 1

        # calculate the calibration value of the current line and add to the sum
        total += cal_val_recovery_v2(current)

        # read the next line from the file
        current = in_file.readline()

    print("Sum of calibration values =", total)

    # close file once the program completes
    in_file.close()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
