# Advent of code day 7
# To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards
# that can act like whatever card would make the hand the strongest type possible.
#
# To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same
# order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.
#
# J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now
# considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always
# treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.
#
# Now, the above example goes very differently:
#
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# 32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
# KK677 is now the only two pair, making it the second-weakest hand.
# T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
# With the new joker rule, the total winnings in this example are 5905.
#
# Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?


# import counter class from collections module
from collections import Counter


# variables to hold the input hands and bids
hands = []
types = []
bids = []


# read in the input file and use it to update time and distance lists
def parse_file():
    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file and remove the \n
    current = in_file.readline()[0:-1]

    # iterate through file
    while current:
        # add the hand and bid from the current line to the list
        hands.append(current.split(' ', 1)[0])
        bids.append(int(current.split(' ', 1)[1]))

        # read in next line
        current = in_file.readline()[0:-1]

    # close file once the program completes
    in_file.close()


# function to determine the type of each hand
# 1 = 5 of a kind
# 2 = 4 of a kind
# 3 = full house
# 4 = three of a kind
# 5 = two pair
# 6 = one pair
# 7 = high card
def determine_type():
    size = len(hands)

    for i in range(size):

        # convert the hand into a counted list
        x = Counter(hands[i])
        x = x.most_common()

        # find card with he highest number of instances
        curr_type = x[0][1]

        # if the most common card is the joker
        if x[0][0] == 'J' and curr_type < 5:
            # if we have less than 5 jokers, add the 2nd most common type to the jokers
            curr_type += x[1][1]

        # check the list to see if any of the other cards are jokers, and update curr_type accordingly
        for j in range(1, len(x)):
            if x[j][0] == 'J':
                curr_type += x[j][1]
                break

        match curr_type:
            case 5:  # 5 of a kind
                types.append(1)
            case 4:  # 4 of a kind
                types.append(2)
            case 3:
                if x[1][1] == 2:  # full house
                    types.append(3)
                else:  # 3 of a kind
                    types.append(4)
            case 2:
                if x[1][1] == 2:  # two pair
                    types.append(5)
                else:  # one pair
                    types.append(6)
            case 1:  # high card
                types.append(7)


# function to swap elements in the hands/types/bids arrays
def swapper(j):
    types[j], types[j + 1] = types[j + 1], types[j]
    hands[j], hands[j + 1] = hands[j + 1], hands[j]
    bids[j], bids[j + 1] = bids[j + 1], bids[j]


# function to convert a card number to an int
def card_to_num(card):
    ret_val = 0

    if card.isdigit():
        ret_val = int(card)
    else:
        match card:
            case 'A':
                ret_val = 14
            case 'K':
                ret_val = 13
            case 'Q':
                ret_val = 12
            case 'J':
                ret_val = 1
            case 'T':
                ret_val = 10

    return ret_val


# function to determine which hand of same type is stronger
# returns true if hand1 in stronger
def stronger_hand(hand1, hand2):
    for i in range(5):
        card1 = card_to_num(hand1[i])
        card2 = card_to_num(hand2[i])
        if card1 < card2:
            return False
        if card1 > card2:
            return True


# function to sort the bids list based on the corresponding hand
def sort_bids():
    size = len(hands)

    # sort based on the type of hand
    for i in range(size):
        for j in range(0, size - i - 1, 1):
            # if the hand type is the same
            if types[j] == types[j + 1]:
                if stronger_hand(hands[j], hands[j + 1]):
                    swapper(j)

            # if worse hand type, swap
            if types[j] < types[j + 1]:
                swapper(j)


def main():
    # parse the input file
    parse_file()

    # find the type of every hand and update the appropriate list
    determine_type()

    # sort the list of bids
    sort_bids()

    output = 0

    # calculate total winnings
    for i in range(len(bids)):
        output += bids[i] * (i + 1)

    print("Total winnings:", output)


if __name__ == "__main__":
    main()
