import unicodedata
import sys


s = 'python\fis\tawesome\r\n'

print(s)

remap = {
	ord('\t') : ' ',
	ord('\f') : ' ',
	ord('\r') : None,
}

a = s.translate(remap)
print(a)



cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
				if unicodedata.combining(chr(c)))


print(cmb_chrs)

b = unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))

