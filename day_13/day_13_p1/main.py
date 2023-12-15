# Advent of code day 13
# You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully
# analyzing these patterns, you can figure out where the mirrors are!
#
# For example:
#
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between
# two rows or across a vertical line between two columns.
#
# In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns
# point at the line between the columns:
#
# 123456789
#     ><
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#     ><
# 123456789
# In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not
# perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored;
# every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column
# 3 matches 8, 4 matches 7, and 5 matches 6.
#
# The second pattern reflects across a horizontal line instead:
#
# 1 #...##..# 1
# 2 #....#..# 2
# 3 ..##..### 3
# 4v#####.##.v4
# 5^#####.##.^5
# 6 ..##..### 6
# 7 #....#..# 7
# This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8,
# but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row
# 7, row 3 matches row 6, and row 4 matches row 5.
#
# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to
# that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example,
# the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above
# it, a total of 405.
#
# Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of
# your notes?


# global to hold the list of patterns
patterns = []


def parse_file():
    # let python know patterns is global
    global patterns

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the 2nd line in the file
    current = in_file.readline()

    while current:
        next_pattern = []
        while current != "\n" and current:
            next_pattern.append(current[0:-1])

            # read in next line
            current = in_file.readline()

        patterns.append(next_pattern)
        current = in_file.readline()

    # close file once the program completes
    in_file.close()


# function to find the location of a horizontal reflection, if there is one
# returns the line number of the reflection if there is one, zero otherwise
def horz_reflection(pattern):
    line = 0

    # iterate through the rows of the pattern
    for i in range(len(pattern) - 1):
        # check if two adjacent lines are the same
        if pattern[i] == pattern[i + 1]:
            is_mirror = True
            # if the adjacent lines are the same
            for j in range(len(pattern) - i - 1):
                # check if the remaining lines are also the same
                if pattern[i - j] != pattern[i + j + 1]:
                    is_mirror = False
                    break

            # if all the remaining lines in the pattern are the same then we've found match and can break the loop
            if is_mirror:
                line = i + 1
                break

    print(line)
    return line


# transposes a pattern so we can reuse the horz_reflection function to check for vertical reflections too
# returns the transposed pattern
def transpose(pattern):
    transposed = []

    for i in range(len(pattern[0])):
        r = ''
        for j in range(len(pattern)):
            r += pattern[j][i]
        transposed.append(r)

    return transposed


def pattern_printer(pattern):
    for i in range(len(pattern)):
        print(pattern[i], i + 1)


def main():
    # variable to hold the final answer
    sum = 0

    # parse input to a list of patterns
    parse_file()

    h_reflections = 0
    v_reflections = 0

    for i in range(len(patterns)):
        pattern_printer(patterns[i])
        h_reflections += horz_reflection(patterns[i])

        transposed = transpose(patterns[i])
        pattern_printer(transposed)
        v_reflections += horz_reflection(transposed)

    sum = (h_reflections * 100) + v_reflections

    print("Notes summary:", sum)


if __name__ == "__main__":
    main()
