import random
import datetime

motivations = {
    1: "Keep learning.",
    2: "Believe in yourself.",
    3: "Consistency beats talent.",
    4: "Every expert was once a beginner.",
    5: "Dream big and start small."
}

def features():
    print("====== DAILY COMPANION ======")
    print("1. Show Today's Date")
    print("2. Lucky Number")
    print("3. Exit")

    option = int(input("Select the option you want: "))
    return option

option = features()

while option != 3:
    if option == 1:
        today = datetime.datetime.now()
        print("Today's Date:",
              str(today.day) + "/" +
              str(today.month) + "/" +
              str(today.year))

    elif option == 2:
        number = random.randint(1, 5)
        print("Your Lucky Number:", number)
        print("Today's Motivation:")
        print(motivations[number])

    else:
        print("Invalid Option Selected!")

    option = features()

print("Exiting Daily Companion...")