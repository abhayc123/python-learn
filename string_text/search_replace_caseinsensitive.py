import re

text = 'UPPER PYTHON , lower python , Mixed Python'
p = re.findall('python' , text , flags=re.IGNORECASE)

print p


r = re.sub('python','snake',text , flags=re.IGNORECASE)
print r

def matchcase(word):
	def replace(m):
		text = m.group()
		
		if 		text.isupper():
				return word.upper()
		
		elif 	text.islower():
				return word.lower()
		
		elif 	text[0].isupper():
				return word.capitalize()

		else:
				return word

	return replace



res = re.sub('python',matchcase('snake'), text , flags = re.IGNORECASE)

print res


