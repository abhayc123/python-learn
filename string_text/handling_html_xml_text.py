import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

s = 'Element are written as "<tag>text</tag>".'

print(s)
print(html.escape(s))
print(html.escape(s,quote=False))


s = 'Spicy Jalapeño'
u = s.encode('ascii' , errors = 'xmlcharrefreplace')
print(u)


s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print(p.unescape(s))


t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
