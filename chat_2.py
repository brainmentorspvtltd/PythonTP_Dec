helloIntent = ["hello","hi","hey","hi there","hello there"]

while True:
    msg = input("Enter your message : ")

    if msg in helloIntent:
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't Understand")
