import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
res1 = str_pat.findall(text1)

print res1

text2 = 'Computer says "no." Phone says "yes."'
res2 = str_pat.findall(text2)
print res2

str_pat = re.compile(r'\"(.*?)\"')
res3 = str_pat.findall(text2)
print res3