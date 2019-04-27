def is_card(player_cards, field):

    for card in player_cards:
        if is_sendable(card,field):
            return True


def is_sendable(card, field):
    if card ==  ('', 'w') or card == ('', 'W'):
        return True

    elif card[0] == field[0] or card[1] == field[1]:
        return True

    else:
        return False