from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print ('{}(a, b): {}'.format(func.__name__, func(a, b))) 

# Output
# a = 1
# b = 5.0
# lt(a, b): True
# le(a, b): True
# eq(a, b): False
# ne(a, b): True
# ge(a, b): False
# gt(a, b): False