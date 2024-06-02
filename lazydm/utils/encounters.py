# Matrix of XP per level of character
# easy, mendium, hard, deadly
TABLE = [
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


def encounter_level_number_of_players(players: list) -> list:
    """Returns the recommended XP of the encounter

    Args:
        players (list): list of lists where each sublist contains the number of players and their level

    Returns:
        list: a list of recommended xp for encounter
    """
    recommended_xp = []

    try:
        for num_players, level in players:
            recommended = [xp * num_players for xp in TABLE[level - 1]]
            recommended_xp.append(recommended)
    except ValueError:
        return []

    if len(recommended_xp) > 1:
        sums = [0] * len(recommended_xp[0])

        for xp_list in recommended_xp:
            for i in range(len(xp_list)):
                sums[i] += xp_list[i]

        return sums
    else:
        return recommended_xp[0] if recommended_xp else []
