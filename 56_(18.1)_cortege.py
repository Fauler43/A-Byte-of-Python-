Python 3.8.12 (d00b0afd2a5dd3c13fcda75d738262c864c62fa7, Feb 18 2022, 09:53:04)
[PyPy 7.3.8 with MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_error_details():
	return (2, 'описание ошибки №2')

>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'описание ошибки №2'
>>> 
>>> a, *b = [1, 2, 3, 4]
>>> a
1
>>> b
[2, 3, 4]
>>> # Чтобы интерпретировать результат как «(a, <всё остальное>)», нужно просто поставить звёздочку
>>> # Поменять местами два значения в Python быстрее всего можно так:
>>> a = 5; b = 8
>>> a, b = b, a
>>> a, b
(8, 5)
>>> 