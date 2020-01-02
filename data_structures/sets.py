"""
A set is an unordered collection with no duplicate elements.
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Reference:
https://docs.python.org/3/tutorial/datastructures.html#sets
"""

# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary,

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)  # {'apple', 'pear', 'banana', 'orange'} - duplicated removed

print('orange' in basket)  # True
print('crabgrass' in basket)  # False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)  # {'b', 'r', 'd', 'a', 'c'} - unique letters in a
print(a - b)  # {'b', 'd', 'r'} - letters in a but not in b
print(a | b)  # {'c', 'm', 'a', 'l', 'd', 'z', 'b', 'r'} - letters in a or b or both
print(a & b)  # {'c', 'a'} - letters in both a and b
print(a ^ b)  # {'z', 'b', 'r', 'd', 'm', 'l'} - letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'d', 'r'}
