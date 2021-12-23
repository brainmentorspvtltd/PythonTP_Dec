# file = open('file_2.txt','w')
# file = open('file_3.txt','x')
file = open(r'C:\Users\ASUS\file_2.txt','a')

data = "\nThis is python programming"
file.write(data)

# data = ["Hello\n","World\n","This\n","is\n","Python\n"]
# file.writelines(data)

file.close()