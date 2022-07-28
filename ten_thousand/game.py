from game_logic import GameLogic, Banker


def play_game():
    ans = intro()
    if ans == "y":
        start()
    else:
        exit_game()


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")


def exit_game():
    print("Ok. Maybe another time")


def start():
    rnd = 1
    max_rnd = 20
    while rnd <= max_rnd:
        result = start_round(rnd)

        if result == "q":
            break

        rnd += 1

    end_game()


def end_game():
    return print(f"Thanks for playing. You earned {Banker.get_score()} points")


def start_round(rnd):
    print(f"Starting round {rnd}")
    round_points = 0

    dice_shelf = GameLogic.dice_shelf()

    round_result = do_round(dice_shelf)
    choice = round_result[0]
    turn_points = round_result[1]
    round_points += turn_points

    if choice == "q":
        return "q"
    elif choice == "b":
        print(f"You banked {round_points} points in round {rnd}")
        Banker.add_score(round_points)
        print(f"Total score is {Banker.get_score()} points")

    return round_points


def do_round(shelf):
    while True:
        print(f"Rolling {shelf[1]} dice...")
        roll = do_turn(shelf[1])
        print(f"*** {display_roll(roll)} ***")

        keep = input("> ")

        if keep == "q":
            return "q", 0

        shelf = add_to_shelf(keep)

        turn_points = GameLogic.calculate_score(shelf[0])
        print(f"You have {turn_points} unbanked points and {shelf[1]} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        return input("> "), turn_points


def do_turn(num):
    return GameLogic.roll_dice(num)


def display_roll(roll):
    roll_values = []
    for num in roll:
        roll_values.append(str(num))
    formatted_roll = " ".join(roll_values)
    return formatted_roll


def add_to_shelf(keep):
    return GameLogic.dice_shelf(keep)


if __name__ == '__main__':
    play_game()
