############### Strip Special Character ############### 

s = ' hello world \n'
print s.strip()
print s.lstrip()
print s.rstrip()

############### Strip Special Character ############### 

t = '-------hello========'
print t.lstrip('-')
print t.rstrip('=')


s = ' hello  world \n '
s = s.strip()

print s

print s.replace(' ','')


with 	open('simple.txt') as f:
		lines = (line.strip() for line in f)
		for line in lines:
			print line