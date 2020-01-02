"""
The else clause executes when the try block executes without any errors.

The finally block will execute regardless of an exception or not.
Even when a return statement is found elsewhere, this finally block will still be executed.
This is especially useful for clean-up actions.
"""
for i in range(3):
	try:
		y = 1 / i
	except ZeroDivisionError:
		print('Got ZeroDivisionError when i is', i)
	else:
		print('The result for', i, 'is', y)
	finally:
		print("The operation has completed.")
