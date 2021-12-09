#Prime Number - 5,7,11,12,17,23,29...
num = int(input("Enter the number : "))
prime = False
for i in range(2,num//2):
    if num % i == 0:
        #print(f"{num} is not a prime number")
        prime = False
        break
    else:
        #print(f"{num} is a prime number")
        prime = True

if prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
