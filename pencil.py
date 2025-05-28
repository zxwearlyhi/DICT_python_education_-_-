import random

def get_pencils():
    while True:
        pencils = input("How many pencils: ")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
        else:
            return pencils

def get_first_player(players):
    while True:
        name = input(f"Who will be the first ({players[0]}, {players[1]}): ")
        if name in players:
            return name
        else:
            print(f"Choose between '{players[0]}' and '{players[1]}'")

def get_pencils_taken(max_take):
    while True:
        user_input = input()
        if not user_input.isdigit():
            print("Possible values: '1', '2' or '3'")
            continue
        num = int(user_input)
        if num not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
            continue
        return num

def bot_turn(pencils_left):
    remainder = pencils_left % 4
    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    elif remainder == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))

def main():
    # Кількість олівців та перший гравець
    pencils = get_pencils()
    players = ['John', 'Jack']
    first_player = get_first_player(players)
    current_player = first_player

    while pencils > 0:
        print('|' * pencils)
        print(f"{current_player}'s turn:")

        if current_player == 'John':
            taken = get_pencils_taken(min(3, pencils))
            if taken > pencils:
                print("Too many pencils were taken")
                continue
        else:  # bot
            taken = bot_turn(pencils)
            print(taken)

        pencils -= taken
        # Зміна черги
        current_player = players[1] if current_player == players[0] else players[0]

    # Виграв той, хто останній не ходив
    print(f"{current_player} won!")

if __name__ == "__main__":
    main()
