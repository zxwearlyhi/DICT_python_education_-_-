import random

def get_user_name():
    name = input("Enter your name: > ")
    print(f"Hello, {name}")
    return name

def load_rating(name, filename="rating.txt"):
    rating = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                user, score = line.strip().split()
                if user == name:
                    rating = int(score)
                    break
    except FileNotFoundError:
        pass
    return rating

def save_rating(name, score, filename="rating.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    found = False
    with open(filename, "w") as f:
        for line in lines:
            user, old_score = line.strip().split()
            if user == name:
                f.write(f"{name} {score}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"{name} {score}\n")

def get_options():
    options = input()
    if options.strip() == "":
        return ["rock", "paper", "scissors"]
    else:
        return options.strip().split(",")

def compute_win_condition(options, user_choice, computer_choice):
    num = len(options)
    user_idx = options.index(user_choice)
    win_count = (num - 1) // 2
    losers = [options[(user_idx + i) % num] for i in range(1, win_count + 1)]
    if user_choice == computer_choice:
        return "draw"
    elif computer_choice in losers:
        return "lose"
    else:
        return "win"

def main():
    name = get_user_name()
    score = load_rating(name)
    print("Enter game options separated by comma (leave empty for classic rock-paper-scissors):")
    options = get_options()
    print("Okay, let's start")
    while True:
        user_input = input("> ")
        if user_input == "!exit":
            print("Bye!")
            save_rating(name, score)
            break
        elif user_input == "!rating":
            print(f"Your rating: {score}")
        elif user_input not in options:
            print("Invalid input")
        else:
            computer_choice = random.choice(options)
            result = compute_win_condition(options, user_input, computer_choice)
            if result == "draw":
                print(f"There is a draw ({computer_choice})")
                score += 50
            elif result == "win":
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice}")

if __name__ == '__main__':
    main()
