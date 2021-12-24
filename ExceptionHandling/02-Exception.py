try:
    fnum = int(input("Enter first number : "))
    snum = int(input("Enter second number : "))

    add = fnum + snum
    sub = fnum - snum
    div = fnum / snum
    mul = fnum * snum

except ValueError:
    print("Invalid Input...")

except ZeroDivisionError:
    print("Cannot divide by zero...")

except BaseException as ex:
    print("Some Exception...")

else:
    name = input("Enter your name : ")
    print("Hello",name)
    print("Sum is", add)
    print("Sub is", sub)
    print("Div is", div)
    print("Mul is", mul)