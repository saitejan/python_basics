def fun():
    # takes input from user, stops here until input comes
    a = input('give some input ')
    return a


# print(fun())


def add_by_default(num, num1=1):
    return num+num1


print(add_by_default(11, 6))  # 17
print(add_by_default(10))  # 11

# print(add_by_default(num=11, num1=6)) # we can also pass params like this for better understanding
