# In the giant field just outside, the springs are arranged into rows. For each row, the condition records show every
# spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is itself
# damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.
#
# However, the engineer that produced the condition records also duplicated some of this information in a different
# format! After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in
# the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the
# entire size of its contiguous group (that is, groups are always separated by at least one operational spring: ####
# would always be 4, never 2,2).
#
# So, condition records with no unknown spring conditions might look like this:
#
# #.#.### 1,1,3
# .#...#....###. 1,1,3
# .#.###.#.###### 1,3,1,6
# ####.#...#... 4,1,1
# #....######..#####. 1,6,5
# .###.##....# 3,2,1
# However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For
# example:
#
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# Equipped with this information, it is your job to figure out how many different arrangements of operational and broken
# springs fit the given criteria in each row.
#
# In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in
# that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken
# (#.#), making the whole row #.#.###.
#
# The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. The last ?
# must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? must hide exactly
# one of the two broken springs. (Neither ?? could be both broken springs or they would form a single contiguous group
# of two; if that were true, the numbers afterward would have been 2,3 instead.) Since each ?? can either be #. or .#,
# there are four possible arrangements of springs.
#
# The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and
# second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run
# of unknown spring conditions have many different ways they could hold groups of two and one broken springs:
#
# ?###???????? 3,2,1
# .###.##.#...
# .###.##..#..
# .###.##...#.
# .###.##....#
# .###..##.#..
# .###..##..#.
# .###..##...#
# .###...##.#.
# .###...##..#
# .###....##.#
# In this example, the number of possible arrangements for each row is:
#
# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements
# Adding all of the possible arrangement counts together produces a total of 21 arrangements.
#
# For each row, count all of the different arrangements of operational and broken springs that meet the given criteria.
# What is the sum of those counts?


# global to hold the spring records
springs = []
counts = []


def parse_file():
    # let python know pipe_map is global
    global springs
    global counts

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the 2nd line in the file and remove the \n
    current = in_file.readline()[0:-1]

    while current:
        springs.append(current.split(' ', 1)[0])

        count = current.split(' ', 1)[1]
        count_tuple = tuple(int(x) for x in count.split(","))
        counts.append(count_tuple)

        # read in next line
        current = in_file.readline()[0:-1]

    # close file once the program completes
    in_file.close()


def count_arrangements(pattern, count):
    # base case
    if not pattern:
        return len(count) == 0

    # if there aren't any more values to check
    if not count:
        return "#" not in pattern

    result = 0

    # check the remainder of the pattern after ".?'
    if pattern[0] in ".?":
        result += count_arrangements(pattern[1:], count)

    if (
            pattern[0] in "#?"
            and count[0] <= len(pattern)
            and "." not in pattern[: count[0]]
            and (count[0] == len(pattern) or pattern[count[0]] != "#")
    ):
        result += count_arrangements(pattern[count[0] + 1:], count[1:])

    return result


def main():
    # variable to hold the total number of arrangements
    arrangements = 0

    # parse input to the list of record and counts
    parse_file()

    print(springs)
    print(counts)

    # iterate through the list of spring records
    for i in range(len(springs)):
        print(springs[i])
        print(counts[i])
        arrangements += count_arrangements(springs[i], counts[i])

    print("Total number of arrangements:", arrangements)


if __name__ == "__main__":
    main()
