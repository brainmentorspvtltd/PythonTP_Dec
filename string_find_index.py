text = "hello world, this is Python Programming"
char = input("Enter the character you want to find : ")

count = text.count(char)
index = 0
for i in range(count):
    index = text.index(char,index)
    print(index)
    index += 1
