"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    match card:
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case '10':
            return 10
        case 'A':
            return 1
        case 'J':
            return 10
        case 'Q':
            return 10
        case 'K':
            return 10
        case _:
            print("Invalid Card")

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two
   


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) == 1 or value_of_card(card_two) == 1:
        return 1
    
    sumCards = value_of_card(card_one) + value_of_card(card_two)
    if sumCards + 11 > 21 :
        return 1
    else:
        return 11
   


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
   
    # If there is an Ace in the hand, consider its alternative value (11)
    if card_one == 'A':
        value_one = 11
    if card_two == 'A':
        value_two = 11

    # If the sum is over 21 and there's an Ace, reduce its value to 1
    if (value_one + value_two) > 21:
        if card_one == 'A':
            value_one = 1
        if card_two == 'A':
            value_two = 1

    # Return True if the sum equals 21
    return (value_one + value_two) == 21
    
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if (value_of_card(card_one) + value_of_card(card_two)) > 8 and (value_of_card(card_one) + value_of_card(card_two))<12:
        return True
    return False
