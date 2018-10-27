Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def charactersWithSpace(string):
	for n in range(0,len(string)):
		print(string[n], end = ' ')

		
>>> charactersWithSpace("Hello")
H e l l o 
>>> def fancy(string):
	for n in range(0,len(string)+1):
		print(string[0:n], end ='\n')

		
>>> fancy("tomorrow")

t
to
tom
tomo
tomor
tomorr
tomorro
tomorrow
>>> import math
>>> [math.factorial(n) for n in range(0,10)]
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
>>> #Roll a dice until you get 6
>>> import random
>>> while True:
	r = random.randint(1,6)
	print(r)
	if r==6:
		break

	
3
3
6
>>> #Define a multiparameter function that takes numbers and returns the average
>>> def Multipara(a,b,c):
	return(a+b+c)/3
Multipara(2,3,6)
SyntaxError: invalid syntax
>>> Multipara(2,3,6)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Multipara(2,3,6)
NameError: name 'Multipara' is not defined
>>> def Multipara(a,b,c):
	return(a+b+c)/3

>>> Multipara(2,3,6)
3.6666666666666665
>>> 
