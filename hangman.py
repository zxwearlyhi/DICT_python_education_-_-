# stage 1

import random


def start_game():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = ['-'] * len(word)
    attempts = 8
    guessed_letters = set()

    print("\nStarting the game!")
    while attempts > 0 and '-' in hidden_word:
        print(f"Word: {''.join(hidden_word)} | Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        # Проверка на валидный ввод
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

    # Проверка на победу или поражение
    if '-' not in hidden_word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"You lost! The word was: {word}")

def main():
    while True:
        print("\nHANGMAN Game")
        choice = input('Type "play" to start or "exit" to quit: ').lower()

        if choice == 'play':
            start_game()
        elif choice == 'exit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please type 'play' or 'exit'.")

if __name__ == "__main__":
    main()
