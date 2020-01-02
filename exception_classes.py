"""
A class in an except clause is compatible with an exception.

if it is the same class or a base class thereof (but not the other way around —
an except clause listing a derived class is not compatible with a base class).
"""


class B(Exception):
	pass


class C(B):
	pass


class D(C):
	pass


"""
C and D are user-defined exception classes.

The following code will print B, C, D in this order:
"""
for cls in [B, C, D]:
	try:
		raise cls()
	except D:
		print('D')
	except C:
		print('C')
	except B:
		print('B')

"""
The first matching except clause (B) will be triggered.

The following code will print B, B, B.
"""
for cls in [B, C, D]:
	try:
		raise cls()
	except B:
		print('B')
	except C:
		print('C')
	except D:
		print('D')
