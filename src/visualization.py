import matplotlib.pyplot as plt


def plot_goal_distribution(df):

    plt.figure()

    plt.hist(df["home_goals"], bins=10)
    plt.title("Home Goals Distribution")

    plt.xlabel("Goals")
    plt.ylabel("Frequency")

    plt.show()


def plot_odds_distribution(df):

    plt.figure()

    plt.hist(df["odds_home"], bins=10)
    plt.title("Home Odds Distribution")

    plt.xlabel("Odds")
    plt.ylabel("Frequency")

    plt.show()