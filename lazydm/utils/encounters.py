# Matrix of XP per level of character
# easy, mendium, hard, mortal
TABELA = [
    [25, 50, 75, 100],
    [50, 100, 150, 200],
    [75, 150, 225, 400],
    [125, 250, 375, 500],
    [250, 500, 750, 1100],
    [300, 600, 900, 1400],
    [350, 750, 1100, 1700],
    [450, 900, 1400, 2100],
    [550, 1100, 1600, 2400],
    [600, 1200, 1900, 2800],
    [800, 1500, 2400, 3600],
    [1000, 2000, 3000, 4500],
    [1100, 2200, 3400, 5100],
    [1250, 2500, 3800, 5700],
    [1400, 2800, 4300, 6500],
    [1600, 3200, 4800, 7200],
    [2000, 3900, 5900, 8800],
    [2100, 4200, 6300, 9500],
    [2400, 4500, 7300, 10900],
    [2800, 5700, 8500, 12700],
]


def encounter_level_number_of_players(players):
    """Returns the the recommended XP of the encounter"""
    for player in players:
        players[player[0]]
    recommended_xp = ...
    return recommended_xp
