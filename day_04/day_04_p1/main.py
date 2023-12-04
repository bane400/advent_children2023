# Advent of code day 4 part 1
# As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appeared in the
# list of winning numbers. The first match makes the card worth one point and each match after the first doubles the
# point value of that card.
# For example:
#
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6,
# 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means
# card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the
# first).


# function to convert an input string like '41 48 83 86 17 ' into a list of integers
def str_to_num(in_line):
    # variable to hold output value
    output = []

    # convert the full string into a list of string numbers
    # for example  " 1 21 53 59 44 " becomes ['1', '21', '53', '59', '44']
    nums = in_line.split(' ')

    # cast the strings into ints and add them to the output
    for i in range(len(nums)):
        # ignores all spaces
        if nums[i] != '':
            output.append(int(nums[i]))

    return output


# function to calculate the number of points in the current card
# the function returns the number of points found in the line
def points_on_card(card):
    # variable to store the total amount of points gained in the current card
    total_matches = 0

    # list to store the strings of winning numbers and numbers we have
    num_strs = card.split('|', 1)

    # convert the two strings into integers
    winners = str_to_num(num_strs[0])
    values = str_to_num(num_strs[1])

    for i in range(len(values)):
        if values[i] in winners:
            total_matches += 1

    if not total_matches:
        return 0
    else:
        return 2 ** (total_matches - 1)


def main():
    # open file to parse
    in_file = open("../firsttest.txt", "rt")

    # final points value
    points = 0

    # read the first line in the file
    current = in_file.readline()
    lines = 0

    # loop to iterate to the end of the file line by line
    while current:
        lines += 1

        # remove the 'Card 1:' portion of the string
        current = current.split(':', 1)[1]

        # Calculate the number of points in the current line and add it to the total points
        # split the string to remove the \n at the end of every line
        points += points_on_card(current[0:-1])

        # read the next line from the file
        current = in_file.readline()

    print("Total number of points =", points)

    # close file once the program completes
    in_file.close()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
