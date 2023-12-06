# Advent of code day 6 part 2
# As the race is about to start, you realize the piece of paper with race times and record distances you got earlier
# actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.
#
# So, the example from before:
#
# Time:      7  15   30
# Distance:  9  40  200
# ...now instead means this:
#
# Time:      71530
# Distance:  940200
# Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530
# milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from
# 14 to 71516 milliseconds and beat the record, a total of 71503 ways!
#
# How many ways can you beat the record in this one much longer race?


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
def num_solutions(curr_time, curr_dist):
    # the number of solutions found
    solutions = 0

    # for each possible time, calculate if it's possible to beat the dist record
    for i in range(curr_time):
        # calculate the distance travelled at the current amount of time
        speed = i
        travel_time = curr_time - i
        travelled = speed * travel_time

        # if the distance travelled beats the current record, increment solutions
        if travelled > curr_dist:
            solutions += 1

    return solutions


def main():
    # parse the input file
    parse_file()

    # get the length of our time/distance lists
    size = len(time)

    # save time and dist as strings
    time_str = ""
    dist_str = ""
    for i in range(size):
        time_str = time_str + str(time[i])
        dist_str = dist_str + str(distance[i])

    # convert them back to ints for processing
    curr_time = int(time_str)
    curr_dist = int(dist_str)

    output = num_solutions(curr_time, curr_dist)

    print("Total number of solutions is", output)


if __name__ == "__main__":
    main()
