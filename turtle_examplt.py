Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
\
>>> t = turtle.Pen()
>>> t.shape("turtle")
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(4):
	print(i)
	t.forward(200)
	t.left(90)

	
0
1
2
3
>>> t.reset()
>>> for i in range(40):
	print(i)
	t.forward(4*i)
	t.left(90)

	
0
1
2
3
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
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
>>> import random
>>> random.randint(1,8)
7
>>> 