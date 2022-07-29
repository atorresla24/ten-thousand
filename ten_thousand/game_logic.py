import random
from collections import Counter


class Banker:
    score = 0

    def __init__(self):
        pass

    @staticmethod
    def add_score(points):
        Banker.score += points

    @staticmethod
    def get_score():
        return Banker.score


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def dice_shelf(num=""):
        dice = list(num)
        rem = 6 - len(dice)
        return tuple(dice), rem

    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))

        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        score = 0
        str_list = list(tup)
        num = [int(num) for num in str_list]
        roll = Counter(tup).most_common()

        if tup is None:
            tup = [0]

        if len(tup) == 0:
            return score

        # straight
        if len(roll) == 6:
            return 1500

        # 6 of a kind
        if roll[0][1] == 6:
            if roll[0][0] == 1:
                return 4000

            return int(roll[0][0]) * 400

        # 5 of a kind
        elif roll[0][1] == 5:
            if roll[0][0] == 1:
                score += 3000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50

                elif roll[1][0] == 1:
                    score += 100

            else:
                score += int(roll[0][0]) * 300
                return score

        # 4 of a kind
        elif roll[0][1] == 4:
            if roll[0][0] == 1:
                score += 2000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    score += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    score += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    score += 100 * roll[2][1]

            else:
                score += int(roll[0][0]) * 200
                return score

        # double 3 of a kind
        elif len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                if roll[0][0] == 1:
                    score += 1000
                    return score + roll[1][0] * 100

                if roll[1][0] == 1:
                    score += 1000
                    return score + roll[0][0] * 100

                return roll[0][0] * 100 + roll[1][0] * 100

        # 3 of a kind
        elif roll[0][1] == 3:
            if roll[0][0] == 1:
                score += 1000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    score += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    score += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    score += 100 * roll[2][1]

                elif roll[3][0] == 5:
                    score += 50 * roll[3][1]

                elif roll[3][0] == 1:
                    score += 100 * roll[3][1]

            else:
                score += int(roll[0][0]) * 100
                return score

        # 3 pairs
        elif len(roll) > 2:
            if roll[0][1] and roll[1][1] and roll[2][1] == 2:
                score += 1500
                return score

                # handle single 1's and 5's
            one_counter = 0
            five_counter = 0
            for nums in num:
                if nums == 1:
                    one_counter += 1
                if nums == 5:
                    five_counter += 1
            score += one_counter * 100
            score += five_counter * 50

        return score
