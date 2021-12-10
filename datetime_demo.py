Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 ** 2
100
>>> 10 ** 3
1000
>>> 10 ** 4
10000
>>> x = 6
>>> y = 10
>>> x > y
False
>>> x < y
True
>>> x == y
False
>>> x >= y
False
>>> x <= y
True
>>> x != y
True
>>> z = 30
>>> x > y and x > z
False
>>> x > y or x > z
False
>>> x > y
False
>>> x
6
>>> y
10
>>> not x > y
True
>>> x > y
False
>>> 10 > 6
True
>>> 6 > 10
False
>>> not 10 > 6
False
>>> not 6 > 10
True
>>> x = 10
>>> x += 4
>>> x
14
>>> x -= 4
>>> x
10
>>> x *= 4
>>> x
40
>>> x /= 4
>>> x
10.0
>>> x **= 4
>>> x
10000.0
>>> x //= 4
>>> x
2500.0
>>> x
2500.0
>>> for = 4
SyntaxError: invalid syntax
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> text = "hello world"
>>> msg = "hello"
>>> names = ["Ram","Shyam","Amit"]
>>> name = "Sumit"
>>> name in names
False
>>> name = "Amut"
>>> name = "Amit"
>>> name in names
True
>>> msg in text
True
>>> msg not in text
False
>>> x = 10
>>> y = 10
>>> z = x
>>> z1 = 10
>>> id(10)
1799560325712
>>> id(x)
1799560325712
>>> id(y)
1799560325712
>>> id(z)
1799560325712
>>> id(z1)
1799560325712
>>> x == y
True
>>> x is y
True
>>> x = [10,20]
>>> y = [10,20]
>>> x == y
True
>>> x is y
False
>>> id(x)
1799570067200
>>> id(y)
1799580662400
>>> x = 10.5
>>> y = 10.5
>>> id(x)
1799579825264
>>> id(y)
1799579826320
>>> id(10.5)
1799579826576
>>> id(10.5)
1799579825296
>>> x = 10,20
>>> y = 10,20
>>> x
(10, 20)
>>> y
(10, 20)
>>> x == y
True
>>> x is y
False
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonDec/chat_1.py
Enter your message : hello
Hello User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonDec/chat_1.py
Enter your message : hello
Hello User
Enter your message : hey
I don't Understand
Enter your message : hi
I don't Understand
Enter your message : bye
Bye User
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2021, 12, 10, 11, 22, 12, 478201)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 12, 10, 11, 23, 59, 715757)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2021, 12, 10, 11, 27, 39, 59886)
>>> dt.now().date()
datetime.date(2021, 12, 10)
>>> date = dt.now().date()
>>> print(date)
2021-12-10
>>> time = dt.now().time()
>>> print(time)
11:28:02.580021
>>> date.strftime("%d/%m/%y")
'10/12/21'
>>> date.strftime("%d/%m/%Y")
'10/12/2021'
>>> date.strftime("%d/%M/%Y")
'10/00/2021'
>>> date.strftime("%d/%m/%Y")
'10/12/2021'
>>> date.strftime("%d/%m/%Y, %p")
'10/12/2021, AM'
>>> date.strftime("%d/%m/%Y, %a")
'10/12/2021, Fri'
>>> date.strftime("%d/%m/%Y, %A")
'10/12/2021, Friday'
>>> date.strftime("%d, %b, %Y, %A")
'10, Dec, 2021, Friday'
>>> date.strftime("%d %B, %Y, %A")
'10 December, 2021, Friday'
>>> time.strftime("%H:%M:%S, %p")
'11:28:02, AM'
>>> time = dt.now().time()
>>> time.strftime("%H:%M:%S, %p")
'11:30:50, AM'
>>> 