# Advent of code day 5 part 2
# Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds:
# line actually describes ranges of seed numbers.
#
# The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and
# the second value is the length of the range. So, in the first line of the example above:
#
# seeds: 79 14 55 13
# This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79
# and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55,
# 56, ..., 66, 67.
#
# Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.
#
# In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84,
# fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.
#
# Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest
# location number that corresponds to any of the initial seed numbers?

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
# the function returns the seed pair list
def parse_file():
    # return value of seed pair list
    seed_pairs = []

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
                    seeds = str_to_num(current.split(':', 1)[1])
                    # split the seed list into pairs and add to seed pairs
                    for i in range(0, len(seeds), 2):
                        pair = (seeds[i], seeds[i + 1])
                        seed_pairs.append(pair)

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

    return seed_pairs


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


# uses the mappings to convert a seed value to a location
def seed_to_location(seed):
    location = 0

    # convert seeds to soil
    location = convert(seed, s2s_map)

    # convert soil to fertilizer
    location = convert(location, s2f_map)

    # convert fertilizer to water
    location = convert(location, f2w_map)

    # convert water to light
    location = convert(location, w2l_map)

    # convert light to temp
    location = convert(location, l2t_map)

    # convert temp to humidity
    location = convert(location, t2h_map)

    # convert humidity to location
    location = convert(location, h2l_map)

    return location


def main():
    # parse the input file
    seed_pairs = parse_file()
    print(seed_pairs)

    # variable to hold the smallest location value
    # init to the first seed value
    loc = seed_to_location(seed_pairs[0][0])

    # iterate through the seed pairs
    for i in range(len(seed_pairs)):
        for j in range(seed_pairs[i][1]):
            # find the current seed's final location
            test = seed_to_location(seed_pairs[i][0] + j)
            # if the location found is lower than previous then update loc
            if test < loc:
                loc = test

        print("Current lowest is", loc)

    print("The lowest location is", loc)


if __name__ == "__main__":
    main()
