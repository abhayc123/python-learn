import re

#This is just for seperating words 
line = 'abc;xyz,gf,asdf,12,jh '
splitted_result = re.split(r'[;,\s]\s*' , line)
print splitted_result


#This is just for seperating words and special character also 
line = 'abc;xyz,gf,asdf,12,jh '
splitted_result = re.split(r'(;|,|\s)\s*' , line)
print splitted_result

values = splitted_result[::2]
delimiters = splitted_result[1::2] + ['']


# re making a new string 
print("+++++++++joining values and delimiters+++++++++++")
print ''.join(v+d for v,d in zip(values , delimiters))


