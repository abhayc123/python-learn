parts = ['Is','Chicago','Not','Chicago?']

print ' '.join(parts)
print ','.join(parts)
print ':'.join(parts)

a = 'Is Chicago'
b = 'Not Chicago?'

print a + ' ' + b
print('{} {}'.format(a,b))
print(a + ' ' + b)

a = 'Hello' 'World'
print a



# Better concat
print(a + ':' + b )
print(':'.join([a,b]))
# print(a,b,c, sep=':')


def sample():
	yield 'Is'
	yield 'Chicago'
	yield 'Not'
	yield 'Chicago'

te = '   '.join(sample())

print(te)


def combine(source, maxsize):
	parts = []
	size = 0
	print(source)
	for part in source:
		print(part)
		parts.append(part)
		size += len(part)
		print(size)
		if 	size > maxsize:
			yield ''.join(parts)
			parts = []
			size = 0

	yield ''.join(parts)


for part in combine(sample(), 32768):
	# f.write(part)
	print(part)








