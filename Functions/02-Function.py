# Positional Arguments
def sayHello(greet, name="User"):
    print(greet, name)

sayHello("Hello","Ravi")
sayHello("Bye","Pooja")
sayHello("Good Morning")
sayHello("Good Afternoon","Sumit")

# Keyword Arguments
sayHello(name = "Aman", greet = "Bye")
sayHello(greet = "Hello", name = "Naman")

sayHello("Hello")