Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #function
>>> def areaTriangle(base,height):
	return base * height / 2

>>> areaTriangle(3,5)
7.5
>>> areaTriangle._doc_
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    areaTriangle._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> areaTriangle.__doc__
>>> 
>>> help(areaTriangle)
Help on function areaTriangle in module __main__:

areaTriangle(base, height)

>>> print(areaTriangle.__doc__)
None
>>> # Some more list operations
>>> fruits = ['banana', 'apple', 'orange']
>>> # Add an element to the list
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'orange', 'grape']
>>> exoticFruits = ['papaya','passion']
>>> allFruits = fruits + exotic
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    allFruits = fruits + exotic
NameError: name 'exotic' is not defined
>>> allFruits = fruits + exoticFruits
>>> allFruits
['banana', 'apple', 'orange', 'grape', 'papaya', 'passion']
>>> # Use of randomness
>>> import random
>>> ## A random element of the list
>>> random.choice(allFruits)
'banana'
>>> random.randrange(0,11)
4
>>> def rollDice():
	return random.randrange(1,7)

>>> rollDice
<function rollDice at 0x111ba4730>
>>> rollDice()
1
>>> for i in range(1,6):
	print(rollDice(),end = ' ')

	
4 6 3 5 4 
>>> for i in range(1,6):
	print(rollDice(), end = '/n')

	
1/n4/n5/n4/n6/n
>>> for i in range(1,6):
	print(rollDice(), end = \n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in range(1,6):
	print(rollDice(), end = '\n')

	
1
3
1
6
5
>>> def rolls(n):
        for i in range(n):
	print(rollDice(), end = '\n')
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def rolls(n):
        for i in range(n):
	    print(rollDice(), end = '\n')
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def rolls(n):
        for i in range(n):
		print(rollDice(), end = '\n')
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def rolls(n):
        for i in range(n):
	    print(rollDice(), end = '\n')
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def rolls(n):
	for i in range(n):
		print(rollDice(), end = '\n')

		
>>> rolls(23)
5
6
4
6
4
1
1
4
6
2
3
2
4
2
3
5
3
2
5
5
2
6
2
>>> allFruits
['banana', 'apple', 'orange', 'grape', 'papaya', 'passion']
>>> #How to check, if 'orange' is in the list
>>> 'orange' in allFruits
True
>>> 'ppo' in allFruits
False
>>> #How to find a position of an elemeny in the list
>>> allFruits.index('papaya')
4
>>> def rolls(n):
	for i in range(n):
		print(rollDice(), end = ' ')

		
>>> rolls(1000)
6 2 4 4 4 3 2 1 3 2 2 3 3 4 5 3 4 2 2 1 2 5 2 6 6 2 4 4 4 5 5 4 3 4 6 5 1 6 5 4 3 6 1 2 2 1 1 2 6 6 4 4 5 1 2 2 1 5 3 1 4 4 3 5 1 2 4 1 1 3 4 5 1 3 3 4 2 4 1 6 5 6 3 3 3 1 2 2 4 5 5 1 2 3 6 1 5 4 3 3 3 2 5 3 6 1 3 4 2 2 5 4 6 2 3 1 3 6 2 3 5 2 5 5 2 4 1 6 5 1 4 4 1 4 1 6 6 5 3 1 6 2 1 2 6 1 3 1 6 1 1 4 4 1 1 6 3 3 2 1 6 3 3 2 1 3 4 5 3 1 5 2 3 4 1 3 1 4 3 3 2 2 3 3 5 4 4 1 3 4 3 2 4 1 3 2 5 4 6 5 5 6 4 2 1 2 5 5 6 3 6 2 2 6 3 4 5 6 4 1 6 3 2 4 1 1 3 1 3 1 1 3 3 6 5 2 3 5 5 3 1 1 1 6 4 6 1 1 1 4 3 6 3 5 6 1 1 5 1 3 2 1 6 6 6 2 3 6 4 6 1 1 4 3 1 1 3 2 5 1 1 4 1 3 1 1 2 4 4 5 4 6 2 4 2 5 4 3 3 2 2 4 2 4 5 5 2 4 4 5 5 1 1 4 6 3 3 2 5 2 1 5 5 3 2 5 2 1 6 3 6 1 2 5 2 1 5 2 4 1 2 4 1 1 4 6 1 3 2 2 6 3 6 5 4 6 5 4 5 2 2 4 2 5 3 5 3 2 4 4 1 4 4 4 2 3 5 1 3 6 2 2 1 1 2 4 3 1 1 1 2 1 4 4 6 4 4 5 2 1 6 2 6 1 5 1 3 4 5 3 1 1 6 3 4 5 5 3 4 1 6 4 4 2 6 2 5 3 2 5 6 5 6 1 5 6 1 6 2 2 1 3 3 2 4 1 4 5 4 2 6 1 3 4 3 5 1 2 5 1 4 3 4 2 2 6 2 4 4 2 1 4 2 5 4 4 2 1 6 1 4 4 5 3 1 2 4 6 3 4 4 6 3 4 3 5 2 6 4 5 1 2 6 1 1 3 6 1 1 1 6 2 3 1 3 1 5 4 3 6 4 6 2 4 1 1 2 4 2 2 2 5 3 1 2 5 4 5 4 5 6 3 2 1 6 6 3 3 1 2 6 6 3 4 2 2 5 3 2 1 6 5 3 4 2 6 2 6 1 1 5 1 4 2 5 3 5 6 3 3 3 4 3 5 3 1 4 1 3 2 6 4 1 1 2 1 4 5 1 5 3 4 4 1 3 6 6 4 3 2 4 4 3 2 4 1 6 2 2 1 1 4 2 6 1 5 4 2 5 6 3 4 3 3 5 4 3 4 3 6 1 6 2 3 4 2 1 1 4 3 6 6 1 5 1 2 6 4 4 6 4 1 4 4 2 1 5 3 1 2 1 1 5 1 6 2 6 4 2 5 6 2 2 4 3 3 6 6 5 1 4 2 2 2 3 5 6 3 5 3 4 2 6 3 1 4 5 1 1 6 6 1 3 2 1 2 1 3 3 3 3 1 4 1 5 6 3 1 5 1 1 5 2 5 6 4 2 3 3 4 4 1 4 1 2 5 3 1 5 2 3 5 1 2 6 3 1 3 1 6 2 2 3 2 6 4 4 3 6 5 1 6 6 5 3 5 4 1 6 3 5 2 2 4 2 1 1 6 6 6 3 6 5 4 1 5 5 4 5 1 1 6 3 1 3 4 5 2 2 5 1 6 5 1 5 2 6 5 3 3 1 3 1 3 5 1 4 4 5 1 3 5 2 1 6 5 3 2 3 5 1 6 1 4 6 4 1 2 2 4 5 6 6 6 3 5 4 2 4 1 1 2 6 2 5 4 5 2 5 1 4 3 3 3 2 6 5 6 1 6 2 5 5 6 6 3 2 2 1 5 6 1 2 4 4 2 3 6 2 4 4 5 4 1 2 1 1 5 6 3 5 3 3 4 5 2 5 5 1 3 5 1 6 1 5 6 1 5 4 2 4 6 6 1 5 3 4 2 3 4 1 3 6 4 1 2 4 2 1 3 1 5 3 4 4 4 1 6 6 4 4 5 2 2 1 4 2 5 3 6 6 6 3 5 1 1 1 3 4 2 4 3 1 4 5 1 3 3 5 3 3 5 4 4 1 2 1 3 6 6 
>>> #How to remove the index
>>> allFruits.pop(1)
'apple'
>>> allFruits
['banana', 'orange', 'grape', 'papaya', 'passion']
>>> #Add the element to soem position
>>> allFruits.insert(2,'lime')
>>> allFruits
['banana', 'orange', 'lime', 'grape', 'papaya', 'passion']
>>> #while loop
>>> #print the numbers 1, 2,..,13
>>> index = 1
>>> while(index <= 13):
	print ( index)
	index++
	
SyntaxError: invalid syntax
>>> while(index <= 13):
	print ( index)
	index += 1

	
1
2
3
4
5
6
7
8
9
10
11
12
13
>>> index
14
>>> while ( index):
	print(index, end =' ')
	index = index -1

	
14 13 12 11 10 9 8 7 6 5 4 3 2 1 
>>> index
0
>>> #zero is False
>>> 
