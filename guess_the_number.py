import random

cpu = random.randint(1,100)

while True:
    user = int(input("Guess the number : "))
    if cpu == user:
        print("Congrats, You have guessed the number...")
        break
    elif cpu > user:
        print("You have guessed smaller number")
    elif cpu < user:
        print("You have guessed greater number")
