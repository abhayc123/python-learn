import re

text1 = '11/27/2012'
text2 = 'Nov 27 , 2017'


if 	re.match('\d+/\d+/\d+' , text1):
	print('yes')
else:
	print('no')


if 	re.match('\d+/\d+/\d+' , text2):
	print('yes')
else:
	print('no')