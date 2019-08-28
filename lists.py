a = [1, 2, 3, 4, 5]
print(a)  # prints entire array at once
print(*a)  # prints unpacked array
b, c, *d = a
print(b, c, d)  # b = 1, c = 2, d = [3, 4, 5]
e = d*2  # e = [3, 4, 5, 3, 4, 5]
e.insert(4, "sai")
print(e.index("sai"))
e.remove("sai")  # removes "sai"
# print(e.index("sai")) # throws an error
if "sai" in e:  # using if , it will check first if it exists then it will get index
    print(e.index("sai"))
print(e)
a.append(6)  # insert new element at the end
a.pop(4)  # remove 4th index element
a.insert(1, 10)  # insert new element at 1st index
print(a)

del a[3]  # removes 3rd index element
e.clear()  # it becomes an empty list, equivalent to e = []
print(e)  # []
del e  # removes entire list, variable e will be removed
# print(e)  # throws an error,  name 'e' is not defined
