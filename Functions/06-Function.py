def calc():
    x = 10
    y = 20

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    def mul():
        z = x * y
        return z

    # print(add(), sub(), mul())
    # print(sub())
    return add, sub, mul

output = calc()
print(output[0]())
print(output[1]())
print(output[2]())