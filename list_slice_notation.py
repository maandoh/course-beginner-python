"""
Python list slice notation in the format:

	list_of_items[start:stop:step]
"""

if __name__ == '__main__':
	fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

	# Print the last item in the list.
	print(fruits[-1])   # banana

	# Print the last 2 items in the list.
	print(fruits[-2:])  # ['apple', 'banana']

	# Print everything except the last 2 items.
	print(fruits[:-2])  # ['orange', 'apple', 'pear', 'banana', 'kiwi']

	# Print all items in the list, reversed.
	print(fruits[::-1])  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

	# Print the first two items, reversed.
	print(fruits[1::-1])  # ['apple', 'orange']

	# Print the last 2 items, reversed.
	print(fruits[:-3:-1])  # ['banana', 'apple']

	# Print everything except the last two items, reversed.
	print(fruits[-3::-1])  # ['kiwi', 'banana', 'pear', 'apple', 'orange']
