Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def paramSum(*args): 
 print(args) 
 return sum(args)

>>> 
>>> paraSum(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    paraSum(1,2,3,4,5)
NameError: name 'paraSum' is not defined
>>> def paramSum(*args): 
 print(args) 
 return sum(arg)

>>> paramSum(1,2,3,4,5)
(1, 2, 3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    paramSum(1,2,3,4,5)
  File "<pyshell#5>", line 3, in paramSum
    return sum(arg)
NameError: name 'arg' is not defined
>>> def paramSum(*args): 
 print(args) 
 return sum(args)

>>> paramSum(1,2,3,4,5)
(1, 2, 3, 4, 5)
15
>>> def first(*args):
	for each v in *args:
		
SyntaxError: invalid syntax
>>> def first(*args):
	for v in *args:
		
SyntaxError: invalid syntax
>>> def first(*args):
	for v in args:
		print(v[0])

		
>>> first("Hello", "Banh bi", "hihi")
H
B
h
>>> def first(*args):
	for v in args:
		print(v[0], end=".")

		
>>> first("Deo", "NOi","Nuw")
D.N.N.
>>> def firstLetters(*args):
	for a in args:
		print(a[0], end="")

		
>>> firstLetters("nguyen","ngoc", "truc","anh")
nnta
>>> import random 
 
def dashToChar(li, w, c): 
  """Changes the character list li, if character c is in w""" 
  for i in range(len(w)): 
  if w[i] == c: 
  li[i] = c 
  return li 
 
def hangmanGame(times): 
  """Hangman game. times is the number of wrong guesses""" 
  cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx'] 
  ranCat = random.choice(cats) 
  dashed = len(ranCat) * ['-'] 
  while times: 
  print('You have {0} guesses'.format(times)) 
  print(''.join(dashed)) 
  guessed = input('What character? ') 
  if guessed not in ranCat: 
  times -= 1 
  continue 
  dashed = dashToChar(dashed, ranCat, guessed) 
  if '-' not in dashed: 
  return ''.join(dashed) 
  return 'Sorry, you are hanging'
SyntaxError: multiple statements found while compiling a single statement
>>> import random
>>> def dashToChar(li,w,x):
	for i in range(len(w)):
		if w[i] ==c:
			li[i]=c
			return li

		
>>> def hangmanGame(times):
	cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']
	ranCat =  random.choice(cats)
	dashed = len(ranCat)*['-']
	while times:
		print('You have {0} guesses'.format(times))
		print(''.join(dashed))
		guessed = input('What character? ')
		if guessed not in ranCat:
			times -=1
			continue
		dashed = dashToChar(dashed, ranCat, guessed)
		if '-' not in dashed:
			return ''.join(dashed)
		return  'Sorry you are hanging'

	
>>> hangmanGame(6)
You have 6 guesses
----
What character? d
You have 5 guesses
----
What character? u
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    hangmanGame(6)
  File "<pyshell#48>", line 12, in hangmanGame
    dashed = dashToChar(dashed, ranCat, guessed)
  File "<pyshell#30>", line 3, in dashToChar
    if w[i] ==c:
NameError: name 'c' is not defined
>>> def hangmanGame(times):
	cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']
	ranCat =  random.choice(cats)
	dashed = len(ranCat)*['-']
	while times:
		print('You have {0} guesses'.format(times))
		print(''.join(dashed))
		guessed = input('What character? ')
		if guessed not in ranCat:
			times -=1
			continue
		dashed = dashToChar(dashed, ranCat, guessed)
		if '-' not in dashed:
			return ''.join(dashed)
		return  'Sorry you are hanging'

	
>>> hangmanGame(8)
You have 8 guesses
----
What character? i
You have 7 guesses
----
What character? l
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    hangmanGame(8)
  File "<pyshell#51>", line 12, in hangmanGame
    dashed = dashToChar(dashed, ranCat, guessed)
  File "<pyshell#30>", line 3, in dashToChar
    if w[i] ==c:
NameError: name 'c' is not defined
>>> dash = 6*["-"]
>>> dash
['-', '-', '-', '-', '-', '-']
>>> print("".join(dash))
------
>>> print(".".join(dash))
-.-.-.-.-.-
>>> print(".".join(dash))
-.-.-.-.-.-
>>> def hangmanGame(times):
	cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']
	ranCat =  random.choice(cats)
	dashed = len(ranCat)*['-']
	while times:
		print('You have {0} guesses'.format(times))
		print(''.join(dashed))
		guessed = input('What character? ')
		if guessed not in ranCat:
			times -=1
			continue
			dashed = dashToChar(dashed, ranCat, guessed)
		if '-' not in dashed:
			return ''.join(dashed)
		return  'Sorry you are hanging'

	
>>> hangmanGame(6)
You have 6 guesses
-----
What character? e
'Sorry you are hanging'
>>> def hangmanGame(times):
	cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']
	ranCat =  random.choice(cats)
	dashed = len(ranCat)*['-']
	while times:
		print('You have {0} guesses'.format(times))
		print(''.join(dashed))
		guessed = input('What character? ')
		if guessed not in ranCat:
			times -=1
			continue
		dashed = dashToChar(dashed, ranCat, guessed)
		if '-' not in dashed:
			return ''.join(dashed)
		return  'Sorry you are hanging'

	
>>> hangmanGame(6)
You have 6 guesses
-------
What character? e
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    hangmanGame(6)
  File "<pyshell#62>", line 12, in hangmanGame
    dashed = dashToChar(dashed, ranCat, guessed)
  File "<pyshell#30>", line 3, in dashToChar
    if w[i] ==c:
NameError: name 'c' is not defined
>>> word =  "heo"
>>> if v not in word:
	return v
SyntaxError: 'return' outside function
>>> def Heo(word):
	v = input("Hey")
	if v not in word:
		return v

	
>>> Heo("Hello")
Heyo
>>> Heo("Hello")
Heyq
'q'
>>> def hangmanGame(times):
	cats = ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']
	ranCat =  random.choice(cats)
	dashed = len(ranCat)*['-']
	while times:
		print('You have {0} guesses'.format(times))
		print(''.join(dashed))
		guessed = input('What character? ')
		if guessed not in ranCat:
			times -=1
			continue
		else:
			dashed = dashToChar(dashed, ranCat, guessed)
			if '-' not in dashed:
				return ''.join(dashed)
			return  'Sorry you are hanging'

		
>>> hangman(4)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    hangman(4)
NameError: name 'hangman' is not defined
>>> hangmanGame(4)
You have 4 guesses
-------
What character? c
You have 3 guesses
-------
What character? l
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    hangmanGame(4)
  File "<pyshell#75>", line 13, in hangmanGame
    dashed = dashToChar(dashed, ranCat, guessed)
  File "<pyshell#30>", line 3, in dashToChar
    if w[i] ==c:
NameError: name 'c' is not defined
>>> def Ha(*args):
	if args == null:
		return 10
	elif len(args) =1:
		
SyntaxError: invalid syntax
>>> def Ha(*args):
	if args == null:
		return 10
	elif len(args) ==1:
		return args*10
	else:
		for each v in args:
			
SyntaxError: invalid syntax
>>> def Ha(*args):
	if args == null:
		print 10
	elif len(args) ==1:
		print (int(args)*10)
	else:
		for v in args:
			print(v, end="")
			
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(10)?
>>> 
>>> def Ha(*args):
	if args == null:
		print (10)
	elif len(args) ==1:
		print (int(args)*10)
	else:
		for v in args:
			print(v, end="")

			
>>> Ha(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    Ha(1,2,3,4)
  File "<pyshell#90>", line 2, in Ha
    if args == null:
NameError: name 'null' is not defined
>>> def Ha(*args):
	if len(args) == 0:
		print (10)
	elif len(args) ==1:
		print (int(args)*10)
	else:
		for v in args:
			print(v, end="")

			
>>> Ha(1,2,3,4,5)
12345
>>> Ha()
10
>>> Ha(2)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    Ha(2)
  File "<pyshell#93>", line 5, in Ha
    print (int(args)*10)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> def Ha(*args):
	if len(args) == 0:
		print (10)
	elif len(args) ==1:
		print (int(args[0])*10)
	else:
		for v in args:
			print(v, end="")

			
>>> Ha(2)
20
>>> import random as ra
>>> print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)
>>> input()
23
'23'
>>> flips = 0 
heads = 0 
while flips < 1000: 
  if ra.randrange(0, 2) == 1: 
  heads = heads + 1 
  flips = flips + 1
  
SyntaxError: multiple statements found while compiling a single statement
>>> flips =0
>>> heads = 0
>>> while flips < 1000: 
	  if ra.randrange(0, 2) == 1: 
	  heads = heads + 1 
	  flips = flips + 1
	  
SyntaxError: expected an indented block
>>> while flips < 1000:
	if ra.randrange(0,2)  ==1:
		heads = heads + 1
		flips = flips + 1

		
>>> while flips < 1000:
	if ra.randrange(0,2)  ==1:
		heads = heads + 1
		flips = flips + 1
	if flips ==900:
		print('900 flips and there have been ' + str(heads) + ' heads.')
	if flips ==100:
		print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
	if flips ==500:
		print('Half way done, and heads has come up ' + str(heads) + ' times.')

 
>>> print()

>>> print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!') 
print('Were you close?')
SyntaxError: multiple statements found while compiling a single statement
>>> print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!') 

Out of 1000 coin tosses, heads came up 1000 times!
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
			flips = flips +1
	print("heads = {0}".format(heads))
	print("flips = {0}".format(flips))

	
>>> flips(400)
I will flip a coin 400 times. Guess how many times it will come up heads. (Press enter to begin)

heads = 400
flips = 400
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
130
heads = 200
flips = 200
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		flips = flips +1
	print("heads = {0}".format(heads))
	print("flips = {0}".format(flips))

	
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
100
heads = 96
flips = 200
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		flips = flips +1
	print("heads = {0}".format(heads))
	print("flips = {0}".format(flips))

	
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		else:
			flips = flips +1
	print("heads = {0}".format(heads))
	print("flips = {0}".format(flips))

	
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
100
heads = 183
flips = 200
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
	print("Head come {0}".format(heads))

	
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
130
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    flips(200)
  File "<pyshell#148>", line 5, in flips
    while flips < number:
TypeError: '<' not supported between instances of 'function' and 'int'
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		else:
			flips = flips +1
	print("heads = {0}".format(heads))
	print("flips = {0}".format(flips))

	
>>> flips(100)
I will flip a coin 100 times. Guess how many times it will come up heads. (Press enter to begin)
20
heads = 84
flips = 100
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1

			
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
20
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    flips(200)
  File "<pyshell#154>", line 6, in flips
    while flips < number:
TypeError: '<' not supported between instances of 'function' and 'int'
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		else:
			flips = flips +1
	print("heads = {0}".format(heads))

	
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
100
heads = 192
>>> flips(1000)
I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)
570
heads = 943
>>> flips(200)
I will flip a coin 200 times. Guess how many times it will come up heads. (Press enter to begin)
200
heads = 215
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
			flips = flips +1
	print("heads = {0}".format(heads))

	
>>> flips(500)
I will flip a coin 500 times. Guess how many times it will come up heads. (Press enter to begin)
200
heads = 500
>>> flips(500)
I will flip a coin 500 times. Guess how many times it will come up heads. (Press enter to begin)
10
heads = 500
>>> def flips(number):
	print('I will flip a coin {0} times. Guess how many times it will come up heads. (Press enter to begin)'.format(number))
	input()
	flips = 0
	heads = 0
	while flips < number:
		if ra.randrange(0,2) ==1:
			heads = heads +1
		flips = flips +1
	print("heads = {0}".format(heads))

	
>>> flips(400)
I will flip a coin 400 times. Guess how many times it will come up heads. (Press enter to begin)
200
heads = 199
>>> flips(1000)
I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)
570
heads = 493
>>> flips(10000)
I will flip a coin 10000 times. Guess how many times it will come up heads. (Press enter to begin)
23
heads = 4937
>>> flips(10)
I will flip a coin 10 times. Guess how many times it will come up heads. (Press enter to begin)
4
heads = 8
>>> 
