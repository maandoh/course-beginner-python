"""
Function blocks begin with the keyword def followed by the function name and parentheses.

Syntax:

	def name_of_function( parameters ):
	   " function_docstring "
	   function_suite
	   return [expression]
"""

"""
You can call a function by using the following types of formal arguments −

    Required arguments
    Keyword arguments
    Default arguments
    Variable-length arguments

"""


def print_text(text):
	""" This prints a passed string into this function."""
	print(text)


# Pass by value
print_text('Hello, world!')

# Python interpreter is able to use the keywords provided to match the values with parameters.
print_text(text='Hello, world, again!')

"""
A default argument assumes a default value if a value is not provided in the function call for that argument.
"""


def print_text(text='Hello, world!'):
	""" This prints a passed string into this function."""
	print(text)


print_text()

"""
Variable-length arguments takes a dynamic number of arguments, not named in the function definition.
"""


def print_arguments(arg1, *arg_tuple):
	" This prints a variable passed arguments "
	print('Arguments are: ')
	print(arg1)

	for arg in arg_tuple:
		print(arg)


print_arguments('The', 'big', 'brown', 'fox')

"""
Anonymous functions are not declared in the standard manner by using the def keyword.
Use the lambda keyword to create small anonymous functions.
"""
summation_function = lambda arg1, arg2: arg1 + arg2
print('Total:', summation_function(10, 20))