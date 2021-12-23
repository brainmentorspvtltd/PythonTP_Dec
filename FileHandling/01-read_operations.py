file = open('file_1.txt')

# data = file.read()
# data = file.read(20)
# print(data)

# file.seek(20)
# data = file.read(20)
# print(data)

# data = file.readline()
# print(data)

data = file.readlines()
print(data)

file.close()