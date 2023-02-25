Python 3.8.12 (d00b0afd2a5dd3c13fcda75d738262c864c62fa7, Feb 18 2022, 09:53:04)
[PyPy 7.3.8 with MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = []
>>> i.append('item')
>>> repr(i)
"['item']"
>>> eval(repr(i))
['item']
>>> eval(repr(i)) == i
True
>>> 