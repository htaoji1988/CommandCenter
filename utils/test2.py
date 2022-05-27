a = ["aaa", "bbb", 'ccc']

print(list(map(lambda x:{a.index(x):x}, a)))