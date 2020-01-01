"""
Demonstrate some  list methods.

Referred from:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

if __name__ == '__main__':
	fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

	# Return the number of times x appears in the list.
	print(fruits.count('apple'))  # 2
	print(fruits.count('tangerine'))  # 1

	# Return zero-based index in the list of the first item whose value is equal to x.
	# Raises a ValueError if there is no such item.
	print(fruits.index('banana'))  # 3
	print(fruits.index('banana', 4))  # Find next banana starting a position 4: 6

	fruits.reverse()
	print(fruits)

	# Add an item to the end of the list
	fruits.append('grape')
	print(fruits)

	fruits.sort()
	print(fruits)

	# Remove the first item from the list whose value is equal to x.
	# It raises a ValueError if there is no such item.
	removed = fruits.pop()
	print(removed)  # pear

	# Extend the list by appending all the items from the given iterable.
	fruits.extend(['guava', 'tomato'])
	print(fruits)

	# Remove the first item from the list with the given value.
	fruits.remove('orange')
	print(fruits)
