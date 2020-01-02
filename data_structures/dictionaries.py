"""
Dictionary are a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary;

Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
Tuples can be used as keys if they contain only strings, numbers, or tuples;
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key
(You can’t use lists as keys).

Reference:
https://docs.python.org/3/tutorial/datastructures.html#sets
"""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])  # 4098

del tel['sape']
tel['irv'] = 4127
print(tel)  # {'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))  # ['jack', 'guido', 'irv']
print(sorted(tel))  # ['guido', 'irv', 'jack']
print('guido' in tel)  # True
print('jack' not in tel)  # False

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
tel = dict(sape=4139, guido=4127, jack=4098)
print(tel)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
squares = {x: x ** 2 for x in (2, 4, 6)}
print(squares)  # {2: 4, 4: 16, 6: 36}
