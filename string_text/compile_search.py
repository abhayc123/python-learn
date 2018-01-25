import re

text1 = '11/27/2012'
text2 = 'Nov 27 , 2012'

datepat =  re.compile(r'\d+/\d+/\d+')

if 	re.match(r'\d+/\d+/\d+' , text1):
	print 'yes'
else:
	print 'no'


datepat = re.compile(r'\d+/\d+/\d+')
if 	 datepat.match(text1):
	print 'yes'
else:
	print 'no'


text = 'Today is 11/27/2012.PyConf starts 3/13/2013.'
print datepat.findall(text)


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2017')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.groups()

month , day , year = m.groups()

for month , day , year in datepat.findall(text):
	print('{}-{}-{}'.format(year,month,day))


for m in datepat.finditer(text):
	print(m.group())






