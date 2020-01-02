a = 'two'
b = 'three'
c = 'four'

print('one %s three' % a)  # one two three
print('one %s %s' % (a, b))
print('one', a, b)
print('one', a, b, sep='+')
print('one {} three {} five'.format(a, c))
print('one {1} three {0} five'.format(c, a))
print('+{:^10}+'.format(c))  # Value alignment
print('{:+d}'.format(43))  # Signed numbers
print('{a} {b}'.format(**{'a': a, 'b': b}))
print('{:{width}.{prec}f}'.format(3.1428, width=5, prec=2))
