data = {
    "names" : ["John","Sam","Mac","Tom","Nick"],
    "dept" : ["IT","HR","IT","IT","HR"],
    "salary" : [45000,38000,50000,65000,25000]
}

# 1. Get the salary of any specific emp
empName = input("Enter Emp Name : ")
empIndex = data["names"].index(empName)
empSalary = data["salary"][empIndex]
print(f"Salary of {empName} is {empSalary}")

# 2. Get the employees who works in IT Department
print("Employees who works in IT Department")
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        print(data["names"][i])

# 3. Get the average salary of those employees who works in HR dept
# 4. Total salary paid to IT Department

