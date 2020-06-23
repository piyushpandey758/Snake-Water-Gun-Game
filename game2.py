import random
game_item = ["s", "w", "g"]
chances = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t \t Snake, Water, Gun Game \n \n")
print("s for snake\nw for water\ng for gun ")

while no_of_chance < chances:
    inp = input("Snake Water Gun: ")
    randm = random.choice(game_item)

    if inp == randm:
        print('Tie : You Both got 0 Point\n')

    #if user enter s
    if inp == "s" and randm == "g":
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    if inp == "s" and randm == "w":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    #if user enter g
    if inp == "g" and randm == "w":
        computer_point = computer_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    elif inp == "g" and randm == "s":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    #if user enter w
    elif inp == "w" and randm == "s":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    elif inp == "w" and randm == "g":
        human_point = human_point + 1
        print(f"Your guess is {inp} and computer guess is {randm}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")

    #else:
        #print("You have entered wrong Input\n")

    no_of_chance = no_of_chance + 1
    print(f"{chances - no_of_chance} chance left out of {chances}\n")

print("Game Over")

if computer_point > human_point:
    print("Hurray!! Computer Won and Humman Lose\n")

if computer_point < human_point:
    print("Hurray!! Human Won and Computer lose\n")

print("Snake Water Gun")
print(f"Human got {human_point} points and computer got {computer_point} points")
