# Global Scope - variables can be used throughout the program
x = 10
y = 6

# Function Definition
def add():
    # local scope - variables can be used only inside this function scope
    x = 6
    y = 7
    z = x + y
    print("Sum is",z)

# Function call
add()

def sub():
    z = x - y
    print("Sub is",z)

sub()