#1st

num_friends = int(input("Enter the number of friends joining (including you): "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}

    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    print(friends_dict)