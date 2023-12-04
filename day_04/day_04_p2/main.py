# Advent of code day 4 part 1
# Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10
# were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
#
# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So,
# if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the
# original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any
# more cards. (Cards will never make you copy a card past the end of the table.)
# This time, the above example goes differently:
#
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each
# of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of
# card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

# Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2,
# 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example
# pile of scratchcards causes you to ultimately have 30 scratchcards!


# list to hold all ticket, inital and generated
ticket_list = []


# function to append the ticket copies to the end of the list
def ticket_list_update(card, num):
    for i in range(num):
        ticket_list.append(ticket_list[card + i])

# function to get the game number of a line
# returns an integer value
def get_card_num(line):
    output = line.split(':', 1)[0]
    output = output.split(' ', 1)[1]

    return int(output)


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


# function to calculate the number of matches on the current line
# returns the number matches
def num_matches(card):
    # variable to store the total amount of points gained in the current card
    total_matches = 0

    # list to store the strings of winning numbers and numbers we have
    num_strs = card.split('|', 1)

    # convert the two strings into integers
    winners = str_to_num(num_strs[0])
    values = str_to_num(num_strs[1])

    for i in range(len(values)):
        if values[i] in winners:
            total_matches += 1

    return total_matches

def main():
    # open file to parse
    in_file = open("../finaltest.txt", "rt")

    # read the first line in the file
    current = in_file.readline()

    # loop to iterate to the end of the file line by line and store all values in the ticket list
    while current:
        # add the current ticket to the ticket_list
        # split the string to remove the \n at the end of every line
        ticket_list.append(current[0:-1])

        # read the next line from the file
        current = in_file.readline()

    # close file once the program completes
    in_file.close()

    lines = len(ticket_list)
    i = 0
    # iterate through the ticket_list, adding new tickets to the list as we go
    while i < lines:
        # get the current ticket from the list
        current = ticket_list[i]

        # get the card number
        card = get_card_num(current)

        # remove the 'Card 1:' portion of the string
        current = current.split(':', 1)[1]

        # check the number of matches in the card
        num_to_add = num_matches(current)

        # if the number to add is not 0, then we need to add to update match_list
        if num_to_add:
            ticket_list_update(card, num_to_add)

        i += 1
        lines = len(ticket_list)

    print("Total number of lines =", len(ticket_list))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
