# Advent of code day 6
# The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected
# - they're actually toy boats, each with a big button on top. Holding down the button charges the boat, and releasing
# the button allows the boat to move. Boats move faster if their button was held longer, but time spent holding the
# button counts against the total race time. You can only hold the button at the start of the race, and boats don't move
# until the button is released.
#
# For example:
#
# Time:      7  15   30
# Distance:  9  40  200

# This document describes three races:
#
# The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
# The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
# The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

# Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the
# beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.
#
# So, because the first race lasts 7 milliseconds, you only have a few options:
#
# Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it
# will have traveled 0 millimeters by the end of the race.

# Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per
# millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.

# Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5
# milliseconds to move, reaching a total distance of 10 millimeters.

# Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12
# millimeters.

# Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12
# millimeters.

# Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.

# Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.

# Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat
# can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move.
# 0 millimeters.

# Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could
# hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.
#
# In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the
# record, a total of 8 different ways to win.
#
# In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still
# beat the record, a total of 9 ways you could win.
#
# To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this
# example, if you multiply these values together, you get 288 (4 * 8 * 9).
#
# Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers
# together?


# store the time and distance lists
time = []
distance = []


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


# read in the input file and use it to update time and distance lists
def parse_file():
    # tell python that time and distance are global
    global time
    global distance

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file
    current = in_file.readline()

    # iterate through file
    while current:
        which = current.split(':', 1)[0]
        current = current.split(':', 1)[1]
        if which == "Time":
            time = str_to_num(current)
        else:
            distance = str_to_num(current)

        # read in next line
        current = in_file.readline()

    # close file once the program completes
    in_file.close()


# function to determine the number of winning solutions given a specific time/distance pair
# returns the number of solutions
def num_solutions(index):
    # find the time/dist at the passed in index
    curr_time = time[index]
    curr_dist = distance[index]

    # the number of solutions found
    solutions = 0

    # for each possible time, calculate if it's possible to beat the dist record
    for i in range(curr_time):
        # calculate the distance travelled at the current amount of time
        speed = i
        travel_time = curr_time - i
        travelled = speed * travel_time
        print("speed =", speed, "travel time =", travel_time, "dist travelled =", travelled)

        # if the distance travelled beats the current record, increment solutions
        if travelled > curr_dist:
            solutions += 1

    print("Number of solutions is", solutions)
    return solutions


def main():
    # parse the input file
    parse_file()

    # get the length of our time/distance lists
    size = len(time)

    # variable to store our output value
    output = 1

    # iterate through the list and find the number of solutions for each time/dist combo
    for i in range(size):
        output *= num_solutions(i)

    print("All solutions multiplied is", output)


if __name__ == "__main__":
    main()
