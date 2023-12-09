# Advent of Code day 9 part 2
# For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then,
# rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add
# a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.
#
# In particular, here is what the third example history looks like when extrapolating back in time:
#
# 5  10  13  16  21  30  45
#   5   3   3   5   9  15
#    -2   0   2   4   6
#       2   2   2   2
#         0   0   0
# Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most
# history value: 5.
#
# Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the
# second history. Adding all three new values together produces 2.
#
# Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these
# extrapolated values?


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
        # if we're at the bottom row
        if not i:
            prediction = slacsap[index][0]
        else:
            prediction = slacsap[index][0] - prediction

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
