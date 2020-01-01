"""
List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result of some operations applied to
each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain condition.

Reference:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
"""

if __name__ == '__main__':
	# Create a list of squares
	squares = [x ** 2 for x in range(10)]
	print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

	# Nested for-loops in a single line:
	result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
	print(result)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
1
