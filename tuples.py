"""
Refererence:
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
"""
t = 12345, 54321, 'hello!'
print(t[0])  # 12345
print(t)  # (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)  # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
"""
This gives error:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)  # ([1, 2, 3], [3, 2, 1])

"""
A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. 
; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:
"""
# Empty tuples are constructed by an empty pair of parentheses
empty = ()
print(len(empty))  # 0

# a tuple with one item is constructed by following a value with a comma
singleton = 'hello',  # <-- note trailing comma
print(len(singleton))  # 1
print(singleton)  # ('hello', )

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing.
# The reverse operation is called sequence unpacking.
x, y, z = t
print(x)  # 12345
print(y)  # 54321
print(z)  # hello!
