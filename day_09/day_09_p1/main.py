# Advent of Code day 9
# You pull out your handy Oasis And Sand Instability Sensor and analyze your surroundings. The OASIS produces a report
# of many values and how they are changing over time (your puzzle input). Each line in the report contains the history
# of a single value. For example:
#
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# To best protect the oasis, your environmental report should include a prediction of the next value in each history.
# To do this, start by making a new sequence from the difference at each step of your history. If that sequence is not
# all zeroes, repeat this process, using the sequence you just generated as the input sequence. Once all of the values
# in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be.
#
# In the above dataset, the first history is 0 3 6 9 12 15. Because the values increase by 3 each step, the first
# sequence of differences that you generate will be 3 3 3 3 3. Note that this sequence has one fewer value than the
# input sequence because at each step it considers two numbers from the input. Since these values aren't all zero,
# repeat the process: the values differ by 0 at each step, so the next sequence is 0 0 0 0. This means you have enough
# information to extrapolate the history! Visually, these sequences can be arranged like this:
#
# 0   3   6   9  12  15
#   3   3   3   3   3
#     0   0   0   0
# To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences
# between the two values above them, this also means there is now a placeholder in every sequence above it:
#
# 0   3   6   9  12  15   B
#   3   3   3   3   3   A
#     0   0   0   0   0
# You can then start filling in placeholders from the bottom up. A needs to be the result of increasing 3 (the value to
# its left) by 0 (the value below it); this means A must be 3:
#
# 0   3   6   9  12  15   B
#   3   3   3   3   3   3
#     0   0   0   0   0
# Finally, you can fill in B, which needs to be the result of increasing 15 (the value to its left) by 3 (the value
# below it), or 18:
#
# 0   3   6   9  12  15  18
#   3   3   3   3   3   3
#     0   0   0   0   0
# So, the next value of the first history is 18.


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


# function to check if all the elements in a list are equal
# returns true if all elements are equal
def all_equal(check):
    return len(set(check)) <= 1


# function to take in a list of historical values and extrapolate the next one.
# Returns the value
def extrapolate(values):
    # variable to hold the next predicted value in the sequence
    prediction = 0

    # variable to hold a list of all the deltas
    slacsap = []
    slacsap.append(values)

    # iterate until all the elements in the last row are the same
    while not all_equal(slacsap[-1]):
        deltas = []

        # calculate the list of all the deltas between the elements in the list
        for i in range(1, len(slacsap[-1]), 1):
            deltas.append(slacsap[-1][i] - slacsap[-1][i - 1])

        slacsap.append(deltas)

    size = len(slacsap)

    # now that we have the list of all the deltas, we can calculate the extrapolated value
    for i in range(size):
        index = size - i - 1
        prediction += slacsap[index][-1]

    return prediction


def main():
    # variable to hold the sum of all extrapolated values
    total = 0

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file and remove the \n
    current = in_file.readline()[0:-1]

    # iterate through file
    while current:
        values = str_to_num(current)

        total += extrapolate(values)

        # read in next line
        current = in_file.readline()

    # close file once the program completes
    in_file.close()

    print("Sum of extrapolated values is", total)


if __name__ == "__main__":
    main()
