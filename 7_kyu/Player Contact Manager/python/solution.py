"""Player Contact Manager"""


def player_manager(players):
    result = []
    if players:
        for i, item in enumerate(players.split(', ')):
            if i % 2 == 0:
                player = item
            else:
                result.append({'player': player, 'contact': int(item)})
    return result
