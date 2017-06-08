# 5H 5C 6S 7S KD
# Pair of Fives
# 2C 3S 8S 8D TD
# Pair of Eights


def make_card_number_map():
    numbers = {str(n): n for n in range(2, 10)}
    numbers.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13})
    return numbers

CARD_NUMBER_MAP = make_card_number_map()


def map_number(card):
    return CARD_NUMBER_MAP[card[0]]


def get_numbers(hand):
    return [CARD_NUMBER_MAP[card] for card in hand]


def suit(card):
    return card[1]


def get_suits(hand):
    return [suit(card) for card in hand]


def split_hands(line):
    hands = line.split(' ')
    return hands[:5], hands[5:]


def pair(hand):
    hand_numbers = get_numbers(hand)


def two_pair(hand):
    return


def three_kind(hand):
    return


def straight(hand):
    '''Returns high card of stright if present, else None'''
    hand_numbers = get_numbers(hand)
    if hand_numbers == range(hand_numbers[0], 5):
        return hand_numbers[0]
    else:
        return


def flush(hand):
    suits = get_suits(hand)
    if len(set(suits)) == 1:
        return get_numbers(hand)[0]
    else:
        return


def full_house(hand):
    if three_kind(hand) and pair(hand):
        return


def four_kind(hand):
    return


if __name__ == '__main__':
    with open('p054_poker.txt') as f:
        for line in f:
            line = line.strip('\n')
            hand1, hand2 = split_hands(line)
