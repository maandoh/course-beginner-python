if __name__ == '__main__':
	print('My name is', 'George', 'and I am', 42)
	print('hello', 'world', sep='+')
	print("My name is {} and best place to study programming is {}".format('hello', 'world'))
	print("My name is {0} and best place to study programming is {1}".format('hello', 'world'))
	print('{:^20}'.format('journaldev'))
	print('{:+d}'.format(42))
	# Dictionary Formatting
	stark = {'first': 'Ned', 'second': 'Brandon', 'third': 'Rob'}
	print('{first} {third}'.format(**stark))
	# Datetime Formatting
	from datetime import datetime

	print('{:%Y-%m-%d %H:%M}'.format(datetime(2017, 12, 7, 13, 22)))
	# Decimal formatting
	value = '{:{width}.{prec}f}'.format(3.1428, width=5, prec=2)
	print(value)