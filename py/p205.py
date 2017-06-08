import itertools

if __name__ == '__main__':
    pyr_sides = range(1, 5)
    cubic_sides = range(1, 7)
    num_pyr_dice = 9
    num_cubic_dice = 6

    cubic_totals = (sum(combo) for combo in itertools.product(cubic_sides, repeat=num_cubic_dice))
    pyr_totals = (sum(combo) for combo in itertools.product(pyr_sides, repeat=num_pyr_dice))
    matchups = itertools.product(cubic_totals, pyr_totals)

    total_matchups = (len(pyr_sides) ** num_pyr_dice) * (len(cubic_sides) ** num_cubic_dice)
    print("Total matchups: ", total_matchups)

    pyr_wins = sum(1 for (cubic_die, pyr_die) in matchups if pyr_die > cubic_die)
    pyr_win_prob = pyr_wins / total_matchups
    print("Probability of pyramid winning:", pyr_win_prob)
