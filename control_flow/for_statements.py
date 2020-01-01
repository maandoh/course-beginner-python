"""
Python’s for statement iterates over the items of any sequence (a list or a string),
in the order that they appear in the sequence.

"""


def simple_iteration(list_of_items):
	for word in list_of_items:
		print(word)

"""
When using 'enumerate' on a list, you also get the index of the iteration.
"""

def iterate_with_index(list_of_items):
	for (i, word) in enumerate(list_of_items):
		print('Word', i, 'is:', word)


"""
If you do need to iterate over a sequence of numbers, 
the built-in function range() comes in handy. 
"""

"""
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
"""

def print_even_numbers():
	for num in range(2, 10):
		if num % 2 == 0:
			print("Found an even number", num)
			continue

		print("Found a number", num)
	else:
		print('Finished printing event numbers.')


if __name__ == '__main__':
	words = ['the', 'big', 'brown', 'fox']
	simple_iteration(words)
	simple_iteration('banana')

	iterate_with_index(words)
	print_even_numbers()
