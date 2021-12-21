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

ch = int(input("Enter your choice : "))

x = int(input("Enter first num : "))
y = int(input("Enter second num : "))

# Using List
# operations = [add, sub, div, mul]
# operations[ch-1](x,y)

# Using Dictionary
operations = {
    1 : add,
    2 : sub,
    3 : div,
    4 : mul
}
operations.get(ch)(x,y)