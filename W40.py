Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> def get_middle(s):
  s = input('Give me a word')
  length = len(s)
  if length % 2 != 0:
    result = s[length / 2]
  else:
    result = s[(length-1)/2] + s[length/2]
  return result

>>> get_middle
<function get_middle at 0x10671b8c8>
>>> get_middle()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    get_middle()
TypeError: get_middle() missing 1 required positional argument: 's'
>>> def get_middle(s):
  
  length = len(s)
  if length % 2 != 0:
    result = s[length / 2]
  else:
    result = s[(length-1)/2] + s[length/2]
  return result

>>> get_middle('Hei')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    get_middle('Hei')
  File "<pyshell#7>", line 5, in get_middle
    result = s[length / 2]
TypeError: string indices must be integers
>>> def get_middle(s):
  
  length = len(s)
  if length % 2 != 0:
    result = s[length // 2]
  else:
    result = s[(length-1)//2] + s[length//2]
  return result

>>> get_middle('Hei')
'e'
>>> get_middle('Heii')
'ei'
>>> """ “floor” division (rounds down to nearest whole number)"""
' “floor” division (rounds down to nearest whole number)'
>>> def(a,b):
	
SyntaxError: invalid syntax
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = x*9/5 +32
		return print(x + " " +y)

	
>>> ConvertfromCtoF(20,29)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ConvertfromCtoF(20,29)
  File "<pyshell#20>", line 5, in ConvertfromCtoF
    return print(x + " " +y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = round(x*9/5 +32,1)
		return print(str(x) + " " +str(y))

	
>>> ConvertfromCtoF(20,29)
20 68.0
>>> import math
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = round(x*9/5 +32, 1)
		return print(str(x) + " " +str(y))

	
>>> ConvertfromCtoF(20,29)
20 68.0
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		print x
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		print(x)

		
>>> ConvertfromCtoF(20,29)
20
21
22
23
24
25
26
27
28
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = x*9/5 +32
		y1 = round(y,1)
		print(x + " " +y)

		
>>> ConvertfromCtoF(20,30)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ConvertfromCtoF(20,30)
  File "<pyshell#36>", line 6, in ConvertfromCtoF
    print(x + " " +y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = x*9/5 +32
		y1 = round(y,1)
		print(x + \t + y)
		
SyntaxError: unexpected character after line continuation character
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = x*9/5 +32
		y1 = round(y,1)
		print(x," ",y)

		
>>> ConvertfromCtoF(20,30)
20   68.0
21   69.8
22   71.6
23   73.4
24   75.2
25   77.0
26   78.8
27   80.6
28   82.4
29   84.2
>>> def ConvertfromCtoF(a,b):
	""" a and b is the range of Celcius you want to convert"""
	for x in range(a,b):
		y = x*9/5 +32
		y1 = round(y,1)
		print(x,y)

		
>>> ConvertfromCtoF(20,30)
20 68.0
21 69.8
22 71.6
23 73.4
24 75.2
25 77.0
26 78.8
27 80.6
28 82.4
29 84.2
>>> print(f'a
