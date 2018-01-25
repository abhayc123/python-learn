data = b'Hello World'

print(data[0:5])
print(data.startswith(b'Hello'))

print(data.split())

rep = data.replace(b'Hello' , b'Hello Cruel')
print(rep)


#############    ##################

print("++++++++++++++bytearray++++++++++++++")
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello',b'Hello Cruel'))

#############    ##################


data = b'FOO:BAR,SPAM'

import re
re.split('[:,]',data)
print(re.split(b'[:,]',data))



#################### Discussion ################

a = 'Hello World'
print(a[0])

# Same here
b = b'Hello World'
print(b[0])

s = b'Hello world'
print(s)

st = '{:10s} {:10d} {:10.2f}'.format('ACME',100,490.1).encode('ascii')
print(st)
