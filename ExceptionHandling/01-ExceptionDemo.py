try:
    fnum = int(input("Enter first number : "))
    snum = int(input("Enter second number : "))

    add = fnum + snum
    print("Sum is", add)

    sub = fnum - snum
    print("Sub is", sub)

    div = fnum / snum
    print("Div is", div)

    mul = fnum * snum
    print("Mul is", mul)

    file = open('file_1.txt')
    data = file.read()
    print(data)

except ValueError as ex:
    print("Invalid Input...")
    # print(ex)

except ZeroDivisionError as ex:
    print("Cannot divide by zero...")

except BaseException as ex:
    print("Some Exception...", ex)

name = input("Enter your name : ")
print("Hello",name)