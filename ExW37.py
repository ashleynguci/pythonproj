Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #Define a function with no parameters. Three numbers are asked from the user and the average is calculated.
>>> def NoPara():
	a = float(input("Can you give a number: "))
	b = float(input("Can you give a number: "))
	c = float(input("Can you give a number: "))
	return (a+b+c)/3

>>> NoPara()
Can you give a number: 12
Can you give a number: 23
Can you give a number: 43
26.0
>>> #Define a function with one parameter that is your first name (e.g. Mickey). The function writes to the terminal Hello Mickey! 
  def Greeting(name):
	  
SyntaxError: unexpected indent
>>> def Greeting(name):
	name = input("Hey what is your name?")
	return "Hello" + name +"!"

>>> def Greeting(name):
	return "Hello" + name +"!"

>>> Greeting("Ashley")
'HelloAshley!'
>>> def Greeting(name):
	return "Hello " + name +" !"

>>> Greeting("Ashley")
'Hello Ashley !'
>>> 
