import random

num_friends = int(input("Enter the number of friends joining (including you): "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}

    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    total_amount = float(input("Enter the total amount: "))

    share = round(total_amount / num_friends, 2)

    for friend in friends_dict:
        friends_dict[friend] = share

    lucky_choice = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")

    if lucky_choice.lower() == "yes":
        lucky_friend = random.choice(list(friends_dict.keys()))
        print(f"{lucky_friend} is the lucky one!")

        friends_dict[lucky_friend] = 0

        new_share = round(total_amount / (num_friends - 1), 2)

        for friend in friends_dict:
            if friend != lucky_friend:
                friends_dict[friend] = new_share

    else:
        print("No one is going to be lucky")

    print(friends_dict)