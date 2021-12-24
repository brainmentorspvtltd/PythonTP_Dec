def atm():
    balance = 10000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        raise ValueError("Login Failed...Invalid PIN...")

    withdraw = int(input("Enter the amount : "))
    if withdraw > balance:
        raise ValueError("Insufficient Balance...")
    else:
        balance -= withdraw
        print("Transaction Successful...")
        print("Remaining Balance is :", balance)

try:
    atm()
except ValueError as msg:
    print(msg)
    atm()
