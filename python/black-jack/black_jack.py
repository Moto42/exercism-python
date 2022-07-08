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
    if card in ['J', 'Q', 'K']:
        value = 10
    elif card == 'A':
        value = 1
    else:
        value = int(card)
    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one: str - card dealt in hand.  See below for values.
    :param card_two: str - card dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    result = (card_one, card_two)
    if val_one > val_two:
        result = card_one
    if val_one < val_two:
        result = card_two
    return result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - card dealt. See below for values.
    :param card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    val_one = value_of_card(card_one)
    val_one = 11 if val_one == 1 else val_one
    val_two = value_of_card(card_two)
    val_two = 11 if val_two == 1 else val_two

    return 11 if val_one + val_two + 11 <= 21 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: str - card dealt. See below for values.
    :param card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    blackjack = False
    if 'A' in (card_one, card_two) and \
            any(x in ('J', 'Q', 'K', '10') for x in (card_one, card_two)):
        blackjack = True
    return blackjack


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one: str - cards dealt.
    :param card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    return val_one == val_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one: str - first and second cards in hand.
    :param card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    double_down = False
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    val_tuple = (val_one, val_two)

    if 1 in val_tuple and 10 in val_tuple:
        double_down = True
    elif val_one + val_two in (9, 10, 11):
        double_down = True
    return double_down
