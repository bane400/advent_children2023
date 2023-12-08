# Advent of Code day 8
# It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel
# follow the same instructions, you can escape the haunted wasteland!
#
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you
# have to follow the left/right instructions until you reach ZZZ.
#
# This format defines each node of the network individually. For example:
#
# RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In
# this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the
# left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.
#
# Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of
# instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes
# 6 steps to reach ZZZ:
#
# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

# variables to store lr instructions, nodes, and mapping
lr_dir = ""
nodes = []
mapping = []


# read in the input file and use it to update time and distance lists
def parse_file():
    # let python know lr_dir is globla
    global lr_dir

    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file and remove the \n
    lr_dir = in_file.readline()

    # read the 2nd line in the file and remove the \n
    current = in_file.readline()[0:-1]

    # iterate through file
    while current:
        nodes.append(current[0:3])
        mapping.append((current[7:10], current[12:15]))

        # read in next line
        current = in_file.readline()[0:-1]

    # close file once the program completes
    in_file.close()


def main():
    # parse the input file
    parse_file()

    # number of hops
    hops = 0

    # get first direction
    lr_index = 0
    curr_dir = lr_dir[lr_index]
    size = len(lr_dir) - 1

    # get first node
    node_index = nodes.index("AAA")
    curr_node = nodes[node_index]

    # search for the final node
    while curr_node != "ZZZ":
        # update the hops value
        hops += 1

        if curr_dir == 'L':
            curr_node = mapping[node_index][0]
        else:
            curr_node = mapping[node_index][1]

        # find the index of the current node
        node_index = nodes.index(curr_node)

        # get the next direction
        lr_index = (lr_index + 1) % size
        curr_dir = lr_dir[lr_index]

    print("Number of hops is", hops)


if __name__ == "__main__":
    main()
