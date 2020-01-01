def simple_iteration(list_of_items):
	for word in list_of_items:
		print(word)


def iterate_with_index(list_of_items):
	for (i, word) in enumerate(list_of_items):
		print('Word', i, 'is:', word)


def print_even_numbers():
	for num in range(2, 10):
		if num % 2 == 0:
			print("Found an even number", num)
			continue

		print("Found a number", num)

if __name__ == '__main__':
	words = ['the', 'big', 'brown', 'fox']
	simple_iteration(words)
	iterate_with_index(words)
	print_even_numbers()
