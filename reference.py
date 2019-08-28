# Boolean, string, int, tuple are immutables
# sets, dictionary, array will have a reference

friends = ["sai", "har", "nan", "bal"]

# others = friends  # others will just get a reference of friends array
# others.insert(0, "iam")  # this will affect friends array also
# print(friends)  # ['iam', 'sai', 'har', 'nan', 'bal']

# if you want to take a copy of array rather than taking reference , you should use copy method on array
others = friends.copy()  # others will have a copy of friends array
others = list(friends)   # others will have a copy of friends array
others.insert(0, "iam")  # this won't affect friends array
print(friends)  # ['sai', 'har', 'nan', 'bal']
