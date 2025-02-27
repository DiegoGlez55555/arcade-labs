import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")

miles_native = -20
miles_traveled = 0
distance = 20
fatigue = 0
thirst = 0
water = 3
done = False
while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    direction = input("What is your choice? ")
    if direction == "q" or direction == "Q":
        print("Good bye!!")
        done = True
    elif direction == "e" or direction == "E":
        print("Miles traveled:", miles_traveled,"The natives are",distance,"miles behind you. Fatigue: ", fatigue, "Thirst: ", thirst, "Water: ", water)
    elif direction == "d" or direction == "D":
        print("the camel is happy")
        fatigue = 0
        miles_native = miles_native + random.randint(7,14)
        distance = miles_traveled - miles_native
    elif direction == "c" or direction == "C":
        thirst = thirst + random.randint(1,3)
        fatigue = fatigue + random.randint(1,3)
        miles_native = miles_native + random.randint(7, 14)
        distance = miles_traveled - miles_native
        miles_traveled = miles_traveled + random.randint(10, 20)
        print("miles trveled is", miles_traveled)
    elif direction == "b" or direction == "B":
        thirst = thirst + 1
        fatigue = fatigue + 1
        miles_native = miles_native + random.randint(7, 14)
        miles_traveled = miles_traveled + random.randint(5, 12)
        distance = miles_traveled - miles_native
        print("miles trveled is", miles_traveled)
    elif direction == "a" or direction == "A":
        if water > 0:
            thirst = 0
            water = water - 1
        else:
            print("error: out of water")
        miles_native = miles_native + random.randint(7, 14)
        distance = miles_traveled - miles_native
    if random.randint(1,20) == random.randint(1,20):
        print("you faund a oasis")
        water = 3
        thirst = 0
        fatigue = 0
    if thirst > 6:
        print("you died of thirst")
        done = True
    elif thirst > 4:
        print("you are thirsty")
    if fatigue > 8:
        print("Your camel died of fatigue")
        done = True
    elif fatigue > 5:
        print("Your camel is fatigue")
    elif distance < 15:
        print("The natives are getting close!")
    if distance < 0:
        print("The natives catch you")
        done = True
    if miles_traveled > 200:
        print("You win")
        done = True
