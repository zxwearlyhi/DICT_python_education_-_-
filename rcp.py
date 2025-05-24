import random

def get_computer_choice(options):
    return random.choice(options)

def check_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return 'draw'
    # Визначаємо, який знак перемагає який
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    return 'lose'

def main():
    options = ['rock', 'paper', 'scissors']
    scores = {}
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    scores[name] = 0

    while True:
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            break
        elif user_input == '!rating':
            print(f'Your rating: {scores[name]}')
        elif user_input not in options:
            print('Invalid input')
        else:
            computer_choice = get_computer_choice(options)
            result = check_winner(user_input, computer_choice, options)
            if result == 'draw':
                print(f'There is a draw ({user_input})')
                scores[name] += 50
            elif result == 'win':
                print(f'Well done. The computer chose {computer_choice} and failed')
                scores[name] += 100
            else:
                print(f'Sorry, but the computer chose {computer_choice}')

if __name__ == '__main__':
    main()
