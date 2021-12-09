import random

cpu = random.randint(1,100)
counter = 5
while True:
    user = int(input("Guess the number : "))
    if cpu == user:
        print("Congrats, You have guessed the number...")
        break
    elif cpu > user:
        print("You have guessed smaller number")
    elif cpu < user:
        print("You have guessed greater number")

    counter -= 1
    print("Chances left ::",counter)
    if counter == 0:
        print("You lose, Number was :",cpu)
        break
