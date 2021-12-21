# *args - variable length argument
def add(*x):
    # print(x)
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    print("Sum is",sum)

add(4,5)
add(4,3,5,6)
add(3,4,6,9,5,6,8)

# **kwargs - keyword variable length arguments
def person(**details):
    print(details)

person(name="Ram", age=20)
person(name="Nick", age=34, dept="IT", sal=45000)