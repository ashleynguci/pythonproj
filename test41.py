Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/Users/mac365.vn/Documents'
>>> first = input('What is your name')
What is your name
>>> def initial():
	first = input('What is your firstname?')
	last = input('What is your lastname?')
	return first[0] + "." + last[0]

>>> initial()
What is your firstname?Miguel
What is your lastname?Fernandez
'M.F'
>>> loterry = [None] * 7
>>> loterry
[None, None, None, None, None, None, None]
>>> import random
>>> import math
>>> random.randint(1,41)
8
>>> for i in range(loterry.length):
	lottery[i] = random.randint(1,41))

SyntaxError: invalid syntax
>>> for i in range(loterry.length):
	lottery[i] = random.randint(1,41)

	
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for i in range(loterry.length):
AttributeError: 'list' object has no attribute 'length'
>>> def lottery():
	list = []
	for i in range(7):
		list.append(random.randint(1,41))
	return list

>>> lottery
<function lottery at 0x10f6e01e0>
>>> print(lottery())
[8, 2, 28, 40, 30, 23, 22]
>>> print(lottery())
[32, 33, 19, 41, 27, 22, 14]
>>> print(lottery())
[13, 34, 33, 2, 35, 23, 9]
>>> print(lottery())
[22, 15, 16, 25, 3, 21, 36]
>>> print(lottery())
[3, 24, 31, 4, 35, 40, 6]
>>> print(lottery())
[14, 4, 9, 9, 26, 17, 36]
>>> how to make sure every number different
SyntaxError: invalid syntax
>>> def lottery():
	list = []
	for i in range(7):
		list.append(random.randint(1,41)
	return list
			    
SyntaxError: invalid syntax
>>> lottery()
			    
[34, 35, 1, 29, 12, 20, 6]
>>> def lottery():
	list = []
	for i in range(7):
		if random.randint(1,41) != list[i-1]	    
		list.append(random.randint(1,41)
			    
SyntaxError: invalid syntax
>>> def lottery():
	list = []
	for i in range(7):
		if random.randint(1,41) != list[i-1]	    
		list.append(random.randint(1,41)
			    
SyntaxError: invalid syntax
>>> def lottery():
       list = []
       list.append(random.randint(1,41)
       for i in range (6):
		   
SyntaxError: invalid syntax
>>> def lottery():
       list = []
       list.append(random.randint(1,41)
       for i in range (6) :
		   
SyntaxError: invalid syntax
>>> def lottery():
       list = []
       list.append(random.randint(1,41)
       for i in range (6):
		   
SyntaxError: invalid syntax
>>> def l():
		   list = []
		   list.append(random.randint(1,41)
			       for i in range (1,6):
			       
SyntaxError: invalid syntax
>>> 
