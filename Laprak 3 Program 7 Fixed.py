z = [1, 3, 2, 4, 'Alice', 'Bob']
integers = [x for x in z if isinstance(x, int)]
strings = [x for x in z if isinstance(x, str)]

integers.sort()
strings.sort()

z = integers + strings
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = ' Hello World '
spam.strip()
spam.lstrip()
spam.rstrip()

', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
'ABC'.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'.split()
'MyABCnameABCisABCSimon'.split('ABC')
'My name is Simon'.split('m') 

# Output
# [1, 2, 3, 4, 'Alice', 'Bob']
# Hello there!
# How are you?
# I'm doing fine.
# Hello there!
# How are you?
#I'm fine