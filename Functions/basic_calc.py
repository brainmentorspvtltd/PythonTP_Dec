def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

x = int(input("Enter first num : "))
y = int(input("Enter second num : "))

if ch == "1" : add(x,y)
elif ch == "2" : sub(x,y)
elif ch == "3" : div(x,y)
else : mul(x,y)

