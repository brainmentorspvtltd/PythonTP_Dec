Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def counter():
	x = 0
	while True
	
SyntaxError: invalid syntax
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> counter()
1
>>> x = 0
>>> def counter():
	while True:
		x += 1
		return x

	
>>> counter()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    counter()
  File "<pyshell#13>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x00000202C0655EB0>
>>> count = counter()
>>> next(count)
1
>>> next(count)
2
>>> next(count)
3
>>> for i in range(10):
	print(next(count))

	
4
5
6
7
8
9
10
11
12
13
>>> def views():
	print("Hello")
	yield "Bye"
	print("Hello Again..")

	
>>> views()
<generator object views at 0x00000202C0655EB0>
>>> gen = views()
>>> next(gen)
Hello
'Bye'
>>> next(gen)
Hello Again..
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    next(gen)
StopIteration
>>> def counter():
	x = 0
	while x < 10:
		x += 1
		yield x

		
>>> count = counter()
>>> next(count)
1
>>> next(count)
2
>>> next(count)
3
>>> next(count)
4
>>> next(count)
5
>>> next(count)
6
>>> next(count)
7
>>> 7
7
>>> next(count)
8
>>> next(count)
9
>>> next(count)
10
>>> next(count)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    next(count)
StopIteration
>>> def sayHello():
	return "Hello User"

>>> sayHello()
'Hello User'
>>> def sayHello(name):
	return "Hello",name

>>> sayHello("Ravi")
('Hello', 'Ravi')
>>> def sayHello(name):
	return "Hello " + name

>>> sayHello("Ravi")
'Hello Ravi'
>>> lambda name : "Hello " + name
<function <lambda> at 0x00000202C06F5040>
>>> sayHello
<function sayHello at 0x00000202C06D7EE0>
>>> sayHello()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sayHello()
TypeError: sayHello() missing 1 required positional argument: 'name'
>>> lambda name : "Hello " + name
<function <lambda> at 0x00000202C06F7160>
>>> (lambda name : "Hello " + name)("Ravi")
'Hello Ravi'
>>> 