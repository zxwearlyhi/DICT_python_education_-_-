# 1-st stage
print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("\nThe lion looks healthy.")

# 2-nd stage
camel = r"""
The camel habitat...
___.-''''-.
/___  @      |
',,,,.   |  _.'''''''._
     '    | /          
     |    |              \ 
     |     \     _.-'  '-.
     |      '.-'         '.
     |       ',          |
     |        '',        |
      ',,,-,   ':;       '
         ',,| ;,,       ,' ;;
            ! ; !,,,,,,',,; ;:
           : ; !  !  ! ; ; :
           ; ; !  !  ! ; ; ;,
          ; ;  !  !  ! ; ; ;
         ; ;   !  !  ! ; ; ;
         ;,,   !,,!,,! ;,;
          /_I   L_I   L_I
Look at that!
"""

print(camel)

# 3-rd stage
animals = [camel]

while True:
    user_input = input("Please enter the number of the habitat you would like to view: > ").strip()
    if user_input.lower() == "exit":
        print("See you later!")
        break
    elif user_input.isdigit() and int(user_input) == 0:
        print(animals[0])
    else:
        print("Invalid input. Please enter 0 to view the camel or 'exit' to quit.")