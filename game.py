import random
lst = ['s', 'w', 'g']
chance = 10
no_of_chance = 0
my_point = 0
computer = 0
print("\t\t\t\t Snake,Water,Gun Game\n \n")
print("The snake drinks the water, the gun shoots the snake, and gun has no effect on water.")
print("s for snake \nw for water\ng for gun \n")

while no_of_chance < chance:
    _input = input("Snake,Water,Gun:")
    _random = random.choice(lst)

    if _input == _random:
        print("Tie both 0 point to each\n")

    elif _input == "s"and _random == "g":
        computer = computer +1
        print(f"your guess {_input} and computer guess{_random}\n ")
        print("computer win 1 point\n")
        print(f"computer point is {computer} and your point is{my_point} \n")

    elif _input == "s" and _random == "w":
        my_point=my_point + 1
        print(f"your guess{_input} and computer guess is {_random} \n")
        print("you win 1 point \n")
        print(f"computer point is{computer} and your point is{my_point} \n")
    elif _input=="w" and _random=="s":
        computer=computer +1
        print(f"your guess{_input} and computer guess is {computer} \n")
        print("comuter win 1 point")
        print(f"computer point is {computer} and your point is {my_point} \n")
    elif _input=="g" and _random=="s" :
        my_point=my_point +1
        print(f"you guess {_input} and computer guess{computer}")
        print("you win 1 pint \n")
        print(f"computer point is {computer} and your point is{my_point}")
    else:
        print("invalid input!!")
    no_of_chance=no_of_chance +1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("Game over!!")
if computer==my_point:
    print("your score and computer score are equal thats why match is Tie")
elif computer>my_point:
    print("computer win this game")
else:
    print("congrats you win this game")
print(f"your pint is {my_point} and computer point is {computer}")






