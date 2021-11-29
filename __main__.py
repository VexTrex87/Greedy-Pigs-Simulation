DICE_MIN_NUMBER = 1
DICE_MAX_NUMBER = 6

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def _graph(x, y):
    plt.plot(x, y)
    plt.xticks(np.arange(min(x), max(x) + 1, (max(x) + 1) / 10))
    plt.grid()
    plt.show()    

def roll_random_dice():
    TRIALS = 100

    rolls = {}

    for dice_face in range(DICE_MIN_NUMBER, DICE_MAX_NUMBER + 1, 1):
        rolls[dice_face] = 0

    for trial in range(1, TRIALS + 1):
        print(f'Running Trial {trial}...')
        random_number = random.randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
        rolls[random_number] += 1
            
    for number, rolls in rolls.items():
        probability = round(rolls / TRIALS * 100)
        print(f'{number}: {rolls} ({probability}%)')

def play_greedy_pigs_based_on_rolls():
    TRIALS = 10000
    RESET_NUMBER = 5
    MIN_ROLLS = 1
    MAX_ROLLS = 20

    scores_on_rolls = {}
    for rolls in range(MIN_ROLLS, MAX_ROLLS + 1, 1):
        scores_on_rolls[rolls] = 0

    for trial in range(1, TRIALS + 1):
        percent = round(trial / TRIALS * 100, 2)
        print(f'{percent}%')

        for rolls in scores_on_rolls.keys():
            score = 0
            for roll_number in range(1, rolls + 1, 1):
                random_number = random.randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
                if random_number == RESET_NUMBER:
                    score = 0
                    break
                else:
                    score += random_number
            scores_on_rolls[rolls] += score

    for rolls, score in scores_on_rolls.items():
        print(f'{rolls}: {score / TRIALS}')
        scores_on_rolls[rolls] = score / TRIALS
    _graph(scores_on_rolls.keys(), scores_on_rolls.values())

def play_greedy_pigs_based_on_rolls_animation():
    RESET_NUMBER = 5
    MIN_ROLLS = 1
    MAX_ROLLS = 20

    scores_on_rolls = {}
    for rolls in range(MIN_ROLLS, MAX_ROLLS + 1, 1):
        scores_on_rolls[rolls] = 0

    trials_completed = 0
    def run_trial(i):
        nonlocal trials_completed
        trials_completed += 1

        print(f'Running trial {trials_completed}')

        for rolls in scores_on_rolls.keys():
            score = 0
            for roll_number in range(1, rolls + 1, 1):
                random_number = random.randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
                if random_number == RESET_NUMBER:
                    score = 0
                    break
                else:
                    score += random_number
            scores_on_rolls[rolls] += score

        x_values = scores_on_rolls.keys()
        y_values = []
        for score in scores_on_rolls.values():
            y_values.append(score / trials_completed)

        plt.cla()
        plt.bar(x_values, y_values)

    anim = FuncAnimation(plt.gcf(), run_trial, interval=10)
    plt.tight_layout()
    plt.show()

def play_greedy_pigs_based_on_scores():
    TRIALS = 100000
    RESET_NUMBER = 5
    MIN_SCORE = 1
    MAX_SCORE = 50

    scores_on_scores = {}
    for max_score in range(MIN_SCORE, MAX_SCORE + 1, 1):
        scores_on_scores[max_score] = 0

    for trial in range(1, TRIALS + 1):
        percent = round(trial / TRIALS * 100, 2)
        print(f'{percent}%')

        for max_score in scores_on_scores.keys():
            score = 0
            while True:
                random_number = random.randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
                if random_number == RESET_NUMBER:
                    score = 0
                    break
                else:
                    score += random_number

                if score >= max_score:
                    break
            scores_on_scores[max_score] += score

    for max_score, score in scores_on_scores.items():
        print(f'{max_score}: {score / TRIALS}')
        scores_on_scores[max_score] = score / TRIALS
    _graph(scores_on_scores.keys(), scores_on_scores.values())

def play_greedy_pigs_based_on_scores_animation():
    RESET_NUMBER = 5
    MIN_SCORE = 1
    MAX_SCORE = 50

    scores_on_scores = {}
    for max_score in range(MIN_SCORE, MAX_SCORE + 1, 1):
        scores_on_scores[max_score] = 0

    trials_completed = 0
    def run_trial(i):
        nonlocal trials_completed
        trials_completed += 1

        print(f'Running trial {trials_completed}')

        for max_score in scores_on_scores.keys():
            score = 0
            while True:
                random_number = random.randint(DICE_MIN_NUMBER, DICE_MAX_NUMBER)
                if random_number == RESET_NUMBER:
                    score = 0
                    break
                else:
                    score += random_number

                if score >= max_score:
                    break

            scores_on_scores[max_score] += score

        x_values = scores_on_scores.keys()
        y_values = []
        for score in scores_on_scores.values():
            y_values.append(score / trials_completed)

        plt.cla()
        plt.bar(x_values, y_values)

    anim = FuncAnimation(plt.gcf(), run_trial, interval=10)
    plt.tight_layout()
    plt.show()

def __main__():
    play_greedy_pigs_based_on_rolls_animation()

if __name__ == '__main__':
    __main__()
