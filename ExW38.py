Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #9. Define a function to calculate the velocity, when the parameters are distance and time. What is the velocity of the bus from Turku to Helsinki, when the time is 2 h 10 minutes?
>>> def velocity(distance,time):
	"""formula distance/time"""
	return distance / time

>>> """Distance from Hel to Tur is 168.5, 2h10m = 2.167h"""
'Distance from Hel to Tur is 168.5, 2h10m = 2.167h'
>>> velocity(168.5 , 2.167)
77.75726811259807
>>> #10. Define a function to calculate the body mass index of the man with weight w and height h.
>>> def bmical(w,h):
	"""formular w/h**2, with w in kg and m in meter"""
	return w/h**2

>>> bmical(48,1.62)
18.289894833104707
>>> #Define a function, which has a string parameter and returns the first character.
>>> def firstchar( str text):
	
SyntaxError: invalid syntax
>>> len(hellooo)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len(hellooo)
NameError: name 'hellooo' is not defined
>>> len('hellooooo')
9
>>> def firstchar(text):
	return text[0]

>>> firstchar('hello')
'h'
>>> firstchar('Dontworry')
'D'
>>> #Define a function, which checks, if the parameter (string) is a palindrome.
>>> def Palindrom(text):
	"""check if reverse of text is equal with text"""
	if text = text[::-1]:
		
SyntaxError: invalid syntax
>>> def Palindrome(text):
	if text == text[::-1]:
		return True
	return False

>>> Palindrom('tomato')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Palindrom('tomato')
NameError: name 'Palindrom' is not defined
>>> Palindrome('oho')
True
>>> Palindrome('tomato')
False
>>> 
