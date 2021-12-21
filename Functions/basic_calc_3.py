def calc(x,y,opr):
    expression = x + opr + y
    # print(expression)
    result = eval(expression)
    print("Result is",result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice : "))
x = input("Enter first num : ")
y = input("Enter second num : ")

# Using Dictionary
operators = {
    1 : "+",
    2 : "-",
    3 : "/",
    4 : "*"
}

opr = operators.get(ch)
calc(x,y,opr)