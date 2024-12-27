# 1-st stage

def main():
    print("HANGMAN")
    print("The game will be available soon.")

if __name__ == "__main__":
    main()


    # 2-nd stage

    def main():
        print("HANGMAN")

        word = "python"  # Задано слово
        guess = input("Guess the word: > ")  # Запросить ввод от пользователя

        if guess.lower() == word:
            print("You survived!")  # Пользователь угадал слово
        else:
            print("You lost!")  # Пользователь не угадал слово


    if __name__ == "__main__":
        main()

        import random


        # 3-rd stage

        def main():
            print("HANGMAN")

            words = ['python', 'java', 'javascript', 'php']
            word = random.choice(words)
            guess = input("Guess the word: > ")

            if guess.lower() == word:
                print("You survived!")
            else:
                print("You lost!")


        if __name__ == "__main__":
            main()