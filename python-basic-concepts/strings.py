# #Strings
# Strings are immutable sequences of Unicode characters. Python uses UTF-8 encoding by default. The actual type for Python strings is str.
# "Foo"             # double quoted string
# 'Foo'             # single quoted string (equivalent)
# "Hello 'Foo'"     # nested quotes, no need to escape                 
# """               
# Multi-line
# """               # triple quotes form 'idiomatic' multi-line string
print('Unicode rocks 😎')
print(type('Foo'))

a = 'Foo'         # assign 'Foo' to variable a
b = a[0]          # assign the zeroth element of a to b
print(b)          # b is 'F'
a[1] = 'f'        # a is immutable, will throw a TypeError exception
