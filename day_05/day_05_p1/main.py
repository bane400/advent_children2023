# # Advent of code day 5
# --- Day 5: If You Give A Seed A Fertilizer ---
# You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks
# more to you like a farm.
#
# "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.
#
# "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't
# worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks
# into a look of horrified realization.
#
# "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more
# sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you
# please go check it out?"
#
# You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can
# help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble
# making sense of it."
#
# The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use
# with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each
# kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers
# are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
# For example:
#
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4
# The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
#
# The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into
# numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a
# seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to
# use with which seeds, which water to use with which fertilizer, and so on.
#
# Rather than list every source number and its corresponding destination number one by one, the maps describe entire
# ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start,
# the source range start, and the range length.
#
# Consider again the example seed-to-soil map:
#
# 50 98 2
# 52 50 48
# The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line
# means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length,
# but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds
# to soil number 50 and that seed number 99 corresponds to soil number 51.
#
# The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds
# to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53
# corresponds to soil number 55.
#
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to
# soil number 10.
#
# So, the entire list of seed numbers and their corresponding soil numbers looks like this:
#
# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51
# With this map, you can look up the soil number required for each initial seed number:
#
# Seed number 79 corresponds to soil number 81.
# Seed number 14 corresponds to soil number 14.
# Seed number 55 corresponds to soil number 57.
# Seed number 13 corresponds to soil number 13.
# The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that
# needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do
# this, you'll need to convert each seed number through other categories until you can find its corresponding location
# number. In this example, the corresponding types are:
#
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
# So, the lowest location number in this example is 35.

# variables to hold the inital seed list and various maps
mapper = []
s2s_map = []
s2f_map = []
f2w_map = []
w2l_map = []
l2t_map = []
t2h_map = []
h2l_map = []


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


# function to read/parse the input file and put it into the global arrays
def parse_file():
    # tell python that seeds is global
    global mapper

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file
    current = in_file.readline()

    # Take all maps and store locally into lists
    while current:
        # if the first char is not a digit, then we're at a new map
        if not current[0].isdigit():
            map_type = current.split(':', 1)[0]

            match map_type:
                case "seeds":
                    mapper = str_to_num(current.split(':', 1)[1])

                case "seed-to-soil map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        s2s_map.append(str_to_num(current))
                        current = in_file.readline()

                case "soil-to-fertilizer map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        s2f_map.append(str_to_num(current))
                        current = in_file.readline()

                case "fertilizer-to-water map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        f2w_map.append(str_to_num(current))
                        current = in_file.readline()

                case "water-to-light map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        w2l_map.append(str_to_num(current))
                        current = in_file.readline()

                case "light-to-temperature map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        l2t_map.append(str_to_num(current))
                        current = in_file.readline()

                case "temperature-to-humidity map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    while current[0].isdigit():
                        # add the current line to the appropriate map variable
                        t2h_map.append(str_to_num(current))
                        current = in_file.readline()

                case "humidity-to-location map":
                    current = in_file.readline()
                    # while we haven't reached a blank line
                    # some python funkyness here
                    while current.split(' ')[0].isdigit():
                        h2l_map.append(str_to_num(current))
                        current = in_file.readline()

        current = in_file.readline()

    # close file once the program completes
    in_file.close()


# function to convert source location into dest location for a given list
# returns the dest location
def convert(source, mapping):
    dest = -1

    # check all possible mappings
    for i in range(len(mapping)):
        list_begin = mapping[i][1]
        list_end = list_begin + mapping[i][2] - 1

        # source is convertible
        if list_begin <= source <= list_end:
            # calculate the difference between source and destination locations
            delta = mapping[i][0] - mapping[i][1]
            dest = source + delta

            # since we've found a destination then we can break the loop
            break

    # source was not in the conversion table
    if dest == -1:
        dest = source

    return dest


def main():
    # parse the input file
    parse_file()

    # iterate through the seeds
    for i in range(len(mapper)):
        # convert seeds to soil
        mapper[i] = convert(mapper[i], s2s_map)

        # convert soil to fertilizer
        mapper[i] = convert(mapper[i], s2f_map)

        # convert fertilizer to water
        mapper[i] = convert(mapper[i], f2w_map)

        # convert water to light
        mapper[i] = convert(mapper[i], w2l_map)

        # convert light to temp
        mapper[i] = convert(mapper[i], l2t_map)

        # convert temp to humidity
        mapper[i] = convert(mapper[i], t2h_map)

        # convert humidity to location
        mapper[i] = convert(mapper[i], h2l_map)

    print("The lowest location is", min(mapper))


if __name__ == "__main__":
    main()
