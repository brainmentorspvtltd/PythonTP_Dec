Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> employees = ["Ram","IT",45000,"Morning","Delhi","Chennai"]
>>> type(employees)
<class 'list'>
>>> len(employees)
6
>>> employees[0] = "Shyam"
>>> employees
['Shyam', 'IT', 45000, 'Morning', 'Delhi', 'Chennai']
>>> employees = ("Ram","IT",45000,"Morning","Delhi","Chennai")
>>> type(employees)
<class 'tuple'>
>>> employees[0] = "Shyam"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    employees[0] = "Shyam"
TypeError: 'tuple' object does not support item assignment
>>> del employees[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del employees[0]
TypeError: 'tuple' object doesn't support item deletion
>>> employees = {"name":"Ram","dept":"IT","salary":45000,"shift":"Morning","address":"Delhi","branch":"Chennai"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> employees = {"name":"Ram","dept":"IT","salary":45000,"shift":"Morning","address":"Delhi","branch":"Chennai"}
>>> employees
{'name': 'Ram', 'dept': 'IT', 'salary': 45000, 'shift': 'Morning', 'address': 'Delhi', 'branch': 'Chennai'}
>>> employees[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    employees[0]
KeyError: 0
>>> employees.keys()
dict_keys(['name', 'dept', 'salary', 'shift', 'address', 'branch'])
>>> employees["dept"]
'IT'
>>> employees["name"]
'Ram'
>>> employees["name"] = "Shyam"
>>> employees["name"]
'Shyam'
>>> employees
{'name': 'Shyam', 'dept': 'IT', 'salary': 45000, 'shift': 'Morning', 'address': 'Delhi', 'branch': 'Chennai'}
>>> employees = {"names":["X","Y","Z","A","B"], "salary":[45,34,66,78,83],"dept":["IT","HR","Admin","IT","IT"]}
>>> employees
{'names': ['X', 'Y', 'Z', 'A', 'B'], 'salary': [45, 34, 66, 78, 83], 'dept': ['IT', 'HR', 'Admin', 'IT', 'IT']}
>>> employees["names"]
['X', 'Y', 'Z', 'A', 'B']
>>> employees["dept"]
['IT', 'HR', 'Admin', 'IT', 'IT']
>>> zip(employees)
<zip object at 0x0000028D36147900>
>>> list(zip(employees))
[('names',), ('salary',), ('dept',)]
>>> import pandas as pd
>>> pd.DataFrame(employees)
  names  salary   dept
0     X      45     IT
1     Y      34     HR
2     Z      66  Admin
3     A      78     IT
4     B      83     IT
>>> import matplotlib.pyplot as plt
>>> plt.bar(employees["names"], employees["salary"])
<BarContainer object of 5 artists>
>>> plt.show()
>>> import random as rn
>>> 