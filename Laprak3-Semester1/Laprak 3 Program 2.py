m = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
m.sort()
m
print(m)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam
print(spam)

# Output
# ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
# ['a', 'A', 'z', 'Z']