Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #Calculate 53*27 divided by 2.5*3-1
>>> 53*27/(2.5*3-1)
220.15384615384616
>>> #Calculate 2 raised to 100
>>> 2**100
1267650600228229401496703205376
>>> var deg = 45
SyntaxError: invalid syntax
>>> deg == 45
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    deg == 45
NameError: name 'deg' is not defined
>>> deg = 45
>>> rad = deg/180*3.14
>>> rad
0.785
>>> math.sin(45)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    math.sin(45)
NameError: name 'math' is not defined
>>> math.sin(deg)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    math.sin(deg)
NameError: name 'math' is not defined
>>> import math
>>> math.sin(45)
0.8509035245341184
>>> def Magic(x):
	return math.sin(x)**2+math.cos(x)**2

>>> Magic(2)
1.0
>>> Magic(10)
1.0
>>> #Calculate 10 based logarithm of the answer of exercise 2. Take then the integer part of the calculation. What do you notice?
>>> math.log10(2**100)
30.10299956639812
>>> math.log10(30)
1.4771212547196624
>>> math.log10(1)
0.0
>>> def tan(x):
	return math.sin(x)/math.cos(x)

>>> tan(45)
1.6197751905438615
>>> math.sin(45)
0.8509035245341184
>>> math.cos(45)
0.5253219888177297
>>> def hypotenusa(a,b):
	return math.sqrt( a**2+b**2 )

>>> hypotenusa(3,4)
5.0
>>> 
