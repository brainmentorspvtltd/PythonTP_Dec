Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [3,4,3,6,7]
>>> data = [3,4,3,6,7,'hello',10.45]
>>> type(data)
<class 'list'>
>>> len(data)
7
>>> data[0]
3
>>> data[0:4]
[3, 4, 3, 6]
>>> data[0] = 100
>>> data
[100, 4, 3, 6, 7, 'hello', 10.45]
>>> names = []
>>> names.append("Ram")
>>> names.append("Shyam")
>>> names.append("Mohit")
>>> names
['Ram', 'Shyam', 'Mohit']
>>> names.append("Abhay","Ankit","Inderdeep")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names.append("Abhay","Ankit","Inderdeep")
TypeError: list.append() takes exactly one argument (3 given)
>>> names.append(["Abhay","Ankit","Inderdeep"])
>>> names
['Ram', 'Shyam', 'Mohit', ['Abhay', 'Ankit', 'Inderdeep']]
>>> names[-1]
['Abhay', 'Ankit', 'Inderdeep']
>>> names.pop()
['Abhay', 'Ankit', 'Inderdeep']
>>> names
['Ram', 'Shyam', 'Mohit']
>>> names.pop()
'Mohit'
>>> names.extend(["Abhay","Ankit","Inderdeep"])
>>> names
['Ram', 'Shyam', 'Abhay', 'Ankit', 'Inderdeep']
>>> names.pop(3)
'Ankit'
>>> names
['Ram', 'Shyam', 'Abhay', 'Inderdeep']
>>> names + ["Ravi","Jyoti","Pooja"]
['Ram', 'Shyam', 'Abhay', 'Inderdeep', 'Ravi', 'Jyoti', 'Pooja']
>>> names
['Ram', 'Shyam', 'Abhay', 'Inderdeep']
>>> names = names + ["Ravi","Jyoti","Pooja"]
>>> names
['Ram', 'Shyam', 'Abhay', 'Inderdeep', 'Ravi', 'Jyoti', 'Pooja']
>>> names.count('R')
0
>>> names.count('Ram')
1
>>> names.index('Ravi')
4
>>> names.insert(3,'Akshay')
>>> names
['Ram', 'Shyam', 'Abhay', 'Akshay', 'Inderdeep', 'Ravi', 'Jyoti', 'Pooja']
>>> names.remove(0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    names.remove(0)
ValueError: list.remove(x): x not in list
>>> names.remove("Shyam")
>>> names
['Ram', 'Abhay', 'Akshay', 'Inderdeep', 'Ravi', 'Jyoti', 'Pooja']
>>> names.sort()
>>> names
['Abhay', 'Akshay', 'Inderdeep', 'Jyoti', 'Pooja', 'Ram', 'Ravi']
>>> names.sort(reverse=True)
>>> names
['Ravi', 'Ram', 'Pooja', 'Jyoti', 'Inderdeep', 'Akshay', 'Abhay']
>>> for name in names:
	print(name)

	
Ravi
Ram
Pooja
Jyoti
Inderdeep
Akshay
Abhay
>>> for i in range(len(names)):
	print(i, ":", names[i])

	
0 : Ravi
1 : Ram
2 : Pooja
3 : Jyoti
4 : Inderdeep
5 : Akshay
6 : Abhay
>>> for i in range(len(names)):
	if names[i].startswith('R'):
		print(names[i])

		
Ravi
Ram
>>> even = []
>>> for i in range(1,51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> numbers = [for i in range(5)]
SyntaxError: invalid syntax
>>> numbers = [i for i in range(5)]
>>> numbers
[0, 1, 2, 3, 4]
>>> numbers = [i for i in range(1,51) if i % 2 == 0]
>>> numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> numbers = [i for i in range(1,51) if i % 3 == 0 elif i % 3 != 0]
SyntaxError: invalid syntax
>>> numbers = [i for i in range(1,51) if i % 3 == 0 else "NA"]
SyntaxError: invalid syntax
>>> numbers = [i for i in range(1,51) if i % 3 == 0]
>>> numbers
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
>>> numbers = [[i,j] for i in range(5) for j in range(5) if i == j]
>>> numbers
[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
>>> names
['Ravi', 'Ram', 'Pooja', 'Jyoti', 'Inderdeep', 'Akshay', 'Abhay']
>>> dept = ["IT","HR","IT","IT","IT","HR","IT"]
>>> sal = [46000,25000,40000,55000,80000,35000]
>>> names
['Ravi', 'Ram', 'Pooja', 'Jyoti', 'Inderdeep', 'Akshay', 'Abhay']
>>> sal
[46000, 25000, 40000, 55000, 80000, 35000]
>>> dept
['IT', 'HR', 'IT', 'IT', 'IT', 'HR', 'IT']
>>> data = [names, sal, dept]
>>> data
[['Ravi', 'Ram', 'Pooja', 'Jyoti', 'Inderdeep', 'Akshay', 'Abhay'], [46000, 25000, 40000, 55000, 80000, 35000], ['IT', 'HR', 'IT', 'IT', 'IT', 'HR', 'IT']]
>>> data[0]
['Ravi', 'Ram', 'Pooja', 'Jyoti', 'Inderdeep', 'Akshay', 'Abhay']
>>> data[1]
[46000, 25000, 40000, 55000, 80000, 35000]
>>> data[2]
['IT', 'HR', 'IT', 'IT', 'IT', 'HR', 'IT']
>>> data[0][0]
'Ravi'
>>> data[0][1]
'Ram'
>>> data[0][2]
'Pooja'
>>> data[1][2]
40000
>>> data[2][0]
'IT'
>>> 