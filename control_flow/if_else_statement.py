"""
Reference:
https://docs.python.org/3/tutorial/controlflow.html
"""


def print_x_to_text(x):
	if x == '1':
		print('You selected one.')
	elif x == '2':
		print('You selected two.')
	else:
		print('what is x?')


if __name__ == '__main__':
	x = input('Enter an integer:')
	print_x_to_text(x)
