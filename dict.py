_dict = {
    "brand": "RE",
    "model": "Himalaya",
    "year": 2019
}

# for x in _dict:
#     print(x)  # key names...  brand model year

# for x in _dict:
#     print(_dict[x])  # key names... RE Himalaya 2019

# for x in _dict.values():
#     print(x)          # values... RE Himalaya 2019

# for x, y in _dict.items():
#     print(x, y)   # x-key, y-value... brand RE model Himalaya year 2019

# if "model" in _dict:
#     print("Yes, 'model' is one of the keys in the dictionary")


# # to remove particular key, if keydoesn't exist it will throw error, returns removed value
# item = _dict.pop("model")
# if "model" in _dict:
#     _dict.pop("model")

# # to remove particular key, if keydoesn't exist it will throw error
# if "model" in _dict:
#     del _dict["model"]

# _dict.popitem()    # method removes the last inserted item
# print(len(_dict))   # number of key-value pairs

# # 'mydict' will just get a refernce of '_dict'
# # if you change anything in '_dict' it will reflect in 'mydict' or vice-versa
# mydict = _dict

# # below methods make a copy
# mydict = _dict.copy()
# mydict1 = dict(_dict)

# if color key doesn't exist in '_dict' it will inserted , else ignored
# if inserted , x will be 'white', else it will be old value
# x = _dict.setdefault("color", "White")

# # this will be ignored as 'color' already exists. y will be 'white'
# y = _dict.setdefault("color", "Blue")

# x = ('a', 'b', 'c')
# y = 0
# z = dict.fromkeys(x, y)
# print(z) # {'a': 0, 'b': 0, 'c': 0}
# z = dict.fromkeys(x)
# print(z) # {'a': None, 'b': None, 'c': None}
# print(_dict)

# z = dict.fromkeys(_dict)  # dict.fromkeys(any iterable, value for all keys)
# print(z)  # {'brand': None, 'model': None, 'year': None}

# _dict.update({"color": "White", "a": 1})  # .update(any dict or any iterable)
# # {'brand': 'RE', 'model': 'Himalaya', 'year': 2019, 'color': 'White', 'a': 1}
# print(_dict)

# _dict.update([{"color": "White", "a": 1}, {
#              "b": "bb", "c": 2}, {"d": "dd", "e": 4}])
# # {'brand': 'RE', 'model': 'Himalaya', 'year': 2019, 'color': 'a', 'b': 'c', 'd': 'e'}
# print(_dict)

_dict.update([{"color", "White"}, {"c", 2}, {"e", 4}])
# {'brand': 'RE', 'model': 'Himalaya', 'year': 2019, 'color': 'White', 2: 'c', 'e': 4}
print(_dict)  # 2: 'c', this is weird
