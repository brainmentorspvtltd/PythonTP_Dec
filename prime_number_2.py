#Prime Number - 5,7,11,12,17,23,29...
num = int(input("Enter the number : "))

for i in range(2,num//2 + 1):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
