"""
Built-in exceptions:
https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Handling exceptions:
https://docs.python.org/3/tutorial/errors.html#handling-exceptions
"""
while True:
	try:
		x = int(input('Please enter a number:'))
		break
	except ValueError:
		print('Oops!  That was no valid number. Try again...')

"""
A try statement may have more than one except clause.
"""
try:
	# Do something here...
	pass
except (RuntimeError, TypeError, NameError):
	pass
