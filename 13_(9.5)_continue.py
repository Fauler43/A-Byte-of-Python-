Python 3.8.12 (d00b0afd2a5dd3c13fcda75d738262c864c62fa7, Feb 18 2022, 09:53:04)
[PyPy 7.3.8 with MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
	s = input('Введите что-нибудь : ')
	if s == 'выход':
		break
	if len(s) < 3:
		print('Слишком мало')
		continue
	print('Введённая строка достаточной длины')
	# Разные другие действия здесь...

	
Введите что-нибудь : а
Слишком мало
Введите что-нибудь : 12
Слишком мало
Введите что-нибудь : абв
Введённая строка достаточной длины
Введите что-нибудь : абвгд
Введённая строка достаточной длины
Введите что-нибудь : выход
>>> 