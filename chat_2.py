from datetime import datetime as dt

helloIntent = ["hello","hi","hey","hi there","hello there"]
dateIntent = ["date","what's the date","tell me date"]
timeIntent = ["time","what's the time","tell me time"]

while True:
    msg = input("Enter your message : ")

    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime("%d/%m/%y, %A"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%H:%M:%S, %p"))
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't Understand")
