def square(x):
	"""
	Takes a number, and times itself once.
	:param x: any number
	"""
	return x ** 2  # square


if __name__ == '__main__':
	print('Square of 4 is:', square(4))
	print(square.__doc__)
