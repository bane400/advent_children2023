# Advent of Code day 8 part 2
# After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names
# ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends
# with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.
#
# For example:
#
# LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right
# instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this
# process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they
# act like any other node and you continue as normal.) In this example, you would proceed as follows:
#
# Step 0: You are at 11A and 22A.
# Step 1: You choose all of the left paths, leading you to 11B and 22B.
# Step 2: You choose all of the right paths, leading you to 11Z and 22C.
# Step 3: You choose all of the left paths, leading you to 11B and 22Z.
# Step 4: You choose all of the right paths, leading you to 11Z and 22B.
# Step 5: You choose all of the left paths, leading you to 11B and 22C.
# Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
# So, in this example, you end up entirely on nodes that end in Z after 6 steps.
#
# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end
# with Z?

from math import gcd

# variables to store lr instructions, nodes, and mapping
lr_dir = ""
nodes = []
mapping = []


# read in the input file and use it to update time and distance lists
def parse_file():
    # let python know lr_dir is global
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


# function to find the number of hops from one node to another
# function returns the number of hops needed
def find_path(start, end):
    hops = 0
    # get first direction
    lr_index = 0
    curr_dir = lr_dir[lr_index]
    size = len(lr_dir) - 1

    # get first node
    node_index = nodes.index(start)
    curr_node = nodes[node_index]

    # search for the final node
    while curr_node[2] != end[2]:
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

    return hops


def main():
    # parse the input file
    parse_file()

    # set of all the hops
    hops = []

    # find the number of hops its take to get from all the nodes starting ending with A to a node ending with Z
    for i in range(len(nodes)):
        if nodes[i][2] == 'A':
            hops.append(find_path(nodes[i], "ZZZ"))

    # list of all the hops required to loop from all nodes ending in A to a node ending in Z
    # we need to find the point where all the loops converge, which would be the LCM
    print(hops)

    # calculate the LCM of all the hop values
    lcm = 1
    for i in hops:
        lcm = lcm * i // gcd(lcm, i)

    print("Number of hops is", lcm)


if __name__ == "__main__":
    main()
