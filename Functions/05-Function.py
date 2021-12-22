def counter():
    x = 0
    while True:
        x += 1
        yield x

adder = counter()
print(next(adder))
print(next(adder))
print(next(adder))
print(next(adder))