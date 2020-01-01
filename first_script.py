"""
Any code that is not contained within this statement will be executed upon running.
If you’re using your program file as a module, the code that is not in this statement
will also execute upon its import while running the secondary file.
"""

print('This is my first script...')


def my_function():
	print('Hello from my function!')


"""
In Python, '__main__' is the name of the scope where top-level code will execute.
When a program is run from standard input, a script, or from an interactive prompt,
its __name__ is set equal to '__main__'.
"""

if __name__ == '__main__':
	print('This program is started from the command line.')
	my_function()
