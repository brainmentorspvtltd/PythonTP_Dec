# def temp_conv(c):
#     return 9/5 * c + 32
#
# def km_m(km):
#     return km * 1000
#
# def m_km(m):
#     return m / 1000

# f = temp_conv(34.4)
# print(f)
temp = [34.4,23.5,28.7,30.6,29.6,22.11]
# f = []
# for t in temp:
#     f.append(round(temp_conv(t),2))
#
# print(f)
#
kms = [300,230,221,4.5,56.7,55]
# ms = []
# for k in kms:
#     ms.append(km_m(k))
#
# print(ms)

def myMap(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = myMap(lambda c : 9/5 * c + 32, temp)
print(f)
ms = myMap(lambda km : km * 1000, kms)
print(ms)

# f = list(map(temp_conv, temp))
# print(f)
# ms = list(map(km_m, kms))
# print(ms)

f = list(map(lambda c : 9/5 * c + 32, temp))
print(f)

ms = list(map(lambda km : km * 1000, kms))
print(ms)
