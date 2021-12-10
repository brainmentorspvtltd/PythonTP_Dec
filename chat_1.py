while True:
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't Understand")
