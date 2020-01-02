"""
A try statement may have more than one except clause.
"""
try:
	# Do something here...
	pass
except (RuntimeError, TypeError, NameError):
	pass
