Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {"name":"Ram", "salary":45000, "dept":"IT"}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["name"]
'Ram'
>>> data["salary"]
45000
>>> data["dept"]
'IT'
>>> data.keys()
dict_keys(['name', 'salary', 'dept'])
>>> data.values()
dict_values(['Ram', 45000, 'IT'])
>>> data.items()
dict_items([('name', 'Ram'), ('salary', 45000), ('dept', 'IT')])
>>> data
{'name': 'Ram', 'salary': 45000, 'dept': 'IT'}
>>> data["name"] = "Raman"
>>> data
{'name': 'Raman', 'salary': 45000, 'dept': 'IT'}
>>> data["address"] = "Delhi"
>>> data
{'name': 'Raman', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data.pop("dept")
'IT'
>>> data
{'name': 'Raman', 'salary': 45000, 'address': 'Delhi'}
>>> details = {"dept":"IT","ph":7878787878,"designation":"developer"}
>>> data + details
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data + details
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> data.update(details)
>>> data
{'name': 'Raman', 'salary': 45000, 'address': 'Delhi', 'dept': 'IT', 'ph': 7878787878, 'designation': 'developer'}
>>> for key in data:
	print(key)

	
name
salary
address
dept
ph
designation
>>> for key in data:
	print(key,":",data[key])

	
name : Raman
salary : 45000
address : Delhi
dept : IT
ph : 7878787878
designation : developer
>>> for item in data.values():
	print(item)

	
Raman
45000
Delhi
IT
7878787878
developer
>>> data = {"names" : ["Ram","Shyam","Aman"], "dept":["IT","HR","IT"],"sal":[45000,35000,55000]}
>>> data
{'names': ['Ram', 'Shyam', 'Aman'], 'dept': ['IT', 'HR', 'IT'], 'sal': [45000, 35000, 55000]}
>>> data["names"]
['Ram', 'Shyam', 'Aman']
>>> data["sal"]
[45000, 35000, 55000]
>>> data["dept"]
['IT', 'HR', 'IT']
>>> data["names"][0]
'Ram'
>>> data["sal"][0]
45000
>>> data["dept"][0]
'IT'
>>> data = [{"name":"Ram","sal":45000,"dept":"IT"},{"name":"Aman","sal":35000,"dept":"HR"},{"name":"Shyam","sal":55000,"dept":"IT"}]
>>> data[0]
{'name': 'Ram', 'sal': 45000, 'dept': 'IT'}
>>> data[0]["name"]
'Ram'
>>> data[0]["sal"]
45000
>>> data[0]["dept"]
'IT'
>>> data[0]
{'name': 'Ram', 'sal': 45000, 'dept': 'IT'}
>>> data[1]
{'name': 'Aman', 'sal': 35000, 'dept': 'HR'}
>>> data[2]
{'name': 'Shyam', 'sal': 55000, 'dept': 'IT'}
>>> 