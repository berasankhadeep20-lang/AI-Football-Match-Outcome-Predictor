from scipy.stats import poisson


def expected_goals(attack, defense):

    return attack * defense


def win_probabilities(home_lambda, away_lambda):

    max_goals = 6

    home_win = 0
    draw = 0
    away_win = 0

    for i in range(max_goals):
        for j in range(max_goals):

            prob = poisson.pmf(i, home_lambda) * poisson.pmf(j, away_lambda)

            if i > j:
                home_win += prob
            elif i == j:
                draw += prob
            else:
                away_win += prob

    return home_win, draw, away_win