import random

def level_one():
    correct = 0
    for _ in range(5):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        question = f"{x} {operation} {y}"
        answer = eval(str(x) + operation + str(y))
        print(question)
        user_input = input('> ')
        if user_input.strip().lower() == 'no' or not user_input.replace('-', '').isdigit():
            print('Wrong format! Try again.')
            continue
        if int(user_input) == answer:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')
    return correct

def level_two():
    correct = 0
    for _ in range(5):
        x = random.randint(11, 29)
        print(x)
        answer = x ** 2
        user_input = input('> ')
        if user_input.strip().lower() == 'no' or not user_input.replace('-', '').isdigit():
            print('Wrong format! Try again.')
            continue
        if int(user_input) == answer:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')
    return correct

while True:
    print("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29")
    level_input = input('> ')
    if level_input.strip().lower() == 'no':
        exit()
    if level_input not in ['1', '2']:
        print("Incorrect format.")
        continue
    level = int(level_input)
    if level == 1:
        correct = level_one()
    elif level == 2:
        correct = level_two()
    else:
        print('Incorrect format.')
        continue
    print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
    save_input = input('> ')
    if save_input.strip().lower() == 'yes':
        name = input('What is your name?\n> ')
        with open('results.txt', 'a') as f:
            f.write(f"{name}: {correct}/5 in level {level}\n")
        print('The results are saved in "results.txt".')
    break
