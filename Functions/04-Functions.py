def sayHello():
    # print("Hello User")
    msg = "Hello"
    return msg,"User"

# output = sayHello()
# print(output)

# Packing and Unpacking
msg, username = sayHello()
print("Msg : {}, Username : {}".format(msg, username))
