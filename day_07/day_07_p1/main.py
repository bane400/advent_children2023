# Advent of code day 7
# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand
# consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card
# follows this order, where A is the highest and 2 is the lowest.
#
# Every hand is exactly one type. From strongest to weakest, they are:
#
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other
# card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third
# label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each
# other: A23A4
# High card, where all cards' labels are distinct: 23456
# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.
#
# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand.
# If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each
# hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand
# with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the
# fifth.
#
# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger.
# Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both
# hands have the same first and second card).
#
# To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:
#
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid
# multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the
# strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be
# multiplied by 5.
#
# So, the first step is to put the hands in order of strength:
#
# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is
# stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
# Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid
# with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.
#
# Find the rank of every hand in your set. What are the total winnings?


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
        x = Counter(hands[i])
        x = x.most_common()

        # find card with he highest number of instances
        curr_type = x[0][1]

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
                ret_val = 11
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
