# stage 1
number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        name = input("> ")
        friends[name] = 0

# stage 2
    total_amount = float(input("Enter the total amount:\n"))  # Загальна сума
    split_amount = round(total_amount / number_of_friends, 2)  # Сума для кожного друга
