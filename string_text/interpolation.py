import sys

#here we are using simple string and
#passing argument there in format
s = '{name} has {n} messages.'
print(s.format(name='Guido',n=37))



#here we are using Info class
class Info:
	def __init__(self , name , n=None):
		self.name = name 
		self.n = n


#here using format_map for passing
#object of class that contain same
#variable as string required

s = '{name} has {n} messages.'
a = Info('Guido',37)
print(s.format_map(vars(a)))



# Note format_map and format 
#doesn't consider missing value
#Solution : Make a customize dictionary override class

class safesub(dict):
	def __missing__(self , key):
		return '{' + key + '}'

a = Info('Guido')
print(s.format_map(safesub(vars(a))))


#Hiding variable substitution
def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
print(sub('Your favorite color is {color}'))


name = 'Guido'
n = 37
# '%(name) has %(n) messages.' % vars()


import string
s = string.Template('$name has $n message')
print(s.substitute(vars()))




























