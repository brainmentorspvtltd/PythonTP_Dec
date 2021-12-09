# Prime Number - 5,7,11,12,17,23,29...
# print all prime numbers in a given range
min_range = int(input("Enter minimum number : "))
max_range = int(input("Enter maximum number : "))

print(f"Prime numbers b/w {min_range} and {max_range} are :")

for num in range(min_range, max_range+1):
    for i in range(2,num//2 + 1):
        if num % i == 0:
            #print(f"{num} is not a prime number")
            break
    else:
        #print(f"{num} is a prime number")
        print(num, end=', ')
