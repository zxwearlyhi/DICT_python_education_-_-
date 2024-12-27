# 1-st stage
print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

camel = r"""
The camel habitat...
___.-''''-.
/___ @ |
',,,,. | _.'''''''._
' | / \
| \ _.-' \
| '.-' '-.
| ',
| '',
',,-, ':;
',,| ;,, ,' ;;
! ; !'',,,',',,,,'! ; ;:
: ; ! ! ! ! ; ; :;
; ; ! ! ! ! ; ; ;,
; ; ! ! ! ! ; ;
; ; ! ! ! ! ; ;
;,, !,! !,! ;,;
/_I L_I L_I /_I
Look at that!
"""
print(camel)

animals = [camel, lion, deer, goose, bat, rabbit]

# запит номеру тварини
animal_number = int(input("Please enter the number of the habitat you would like to view: "))

# виведення відповідного зображення
print(animals[animal_number - 1])
print("You've reached the end of the program.")

