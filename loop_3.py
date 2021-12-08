'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        #print('*', end='')
        print(j, end='')
    print()
print("===========")

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print("===========")

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')
    print()

print("===========")

'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()

print("===========")


'''
1
2 3
4 5 6
7 8 9 10
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k, end=' ')
    print()

print("===========")







