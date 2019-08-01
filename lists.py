a = [1, 2, 3, 4, 5]
print(a)  # prints entire array at once
print(*a)  # prints unpacked array
b, c, *d = a
print(b, c, d)  # b = 1, c = 2, d = [3, 4, 5]
e = d*2  # e = [3, 4, 5, 3, 4, 5]
print(e)
a.append(6)  # insert new element at the end
a.pop(4)  # remove 4th index element
a.insert(1, 10)  # insert new element at 1st index
print(a)
