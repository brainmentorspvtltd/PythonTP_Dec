Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is Python Programming"
>>> len(text)
39
>>> text[39]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    text[39]
IndexError: string index out of range
>>> text[38]
'g'
>>> text[6]
'w'
>>> text[16]
's'
>>> text[-1]
'g'
>>> text[-20]
's'
>>> text
'hello world, this is Python Programming'
>>> text[0:10]
'hello worl'
>>> text[10]
'd'
>>> text[0:11]
'hello world'
>>> text[:]
'hello world, this is Python Programming'
>>> text[10:]
'd, this is Python Programming'
>>> text[:20]
'hello world, this is'
>>> text[0:20:2]
'hlowrd hsi'
>>> text[0:20:1]
'hello world, this is'
>>> text[10:0]
''
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[::-1]
'gnimmargorP nohtyP si siht ,dlrow olleh'
>>> text[:]
'hello world, this is Python Programming'
>>> text[::]
'hello world, this is Python Programming'
>>> text[::-1]
'gnimmargorP nohtyP si siht ,dlrow olleh'
>>> import random
>>> random.randint(1,100)
57
>>> randint()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    randint()
NameError: name 'randint' is not defined
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> upper(text)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    upper(text)
NameError: name 'upper' is not defined
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.lower()
'hello world, this is python programming'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'HELLO WORLD, THIS IS pYTHON pROGRAMMING'
>>> text
'hello world, this is Python Programming'
>>> text.replace("hello","bye")
'bye world, this is Python Programming'
>>> text
'hello world, this is Python Programming'
>>> text.count('is')
2
>>> text.count('p')
0
>>> text.count('P')
2
>>> text.index('t')
13
>>> text.index('n')
26
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.index('o',31)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    text.index('o',31)
ValueError: substring not found
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonDec/string_find_index.py =
Enter the character you want to find : o
4
7
25
30
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',30)
30
>>> text.find('o',26)
30
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rfind('o')
30
>>> text.rindex('o')
30
>>> text.isdecimal()
False
>>> text.islower()
False
>>> text.isupper()
False
>>> text.split()
['hello', 'world,', 'this', 'is', 'Python', 'Programming']
>>> text.split(' ')
['hello', 'world,', 'this', 'is', 'Python', 'Programming']
>>> text.split(',')
['hello world', ' this is Python Programming']
>>> text = "    hello    "
>>> text.strip()
'hello'
>>> text.lstrip()
'hello    '
>>> text.rstrip()
'    hello'
>>> text.strip()
'hello'
>>> text = "###hello###"
>>> text.strip()
'###hello###'
>>> text.strip('#')
'hello'
>>> text = "###$$$hello###$$$"
>>> text.strip('#$')
'hello'
>>> text.strip('$')
'###$$$hello###'
>>> 