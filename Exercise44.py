Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #Exercise1
>>> def sumUpTo(n):
	return sum(range(n+1))

>>> sumUpTo(5)
15
>>> sumUpTo(100)
5050
>>> #Exercise2
>>> def frame(n,m):
	i = 1
	print("*"*n)
	i = 2
	while i < m:
		print("*"*(n-2)*"*")
		i +=1
	print("*"*n)

	
>>> frame(3,2)
***
***
>>> frame(2,3)
**
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    frame(2,3)
  File "<pyshell#15>", line 6, in frame
    print("*"*(n-2)*"*")
TypeError: can't multiply sequence by non-int of type 'str'
>>> def frame(n,m):
	i = 1
	print("*"*n)
	i = 2
	while i < m:
		print('*' + " "*(n-2)+'*')
		i +=1
	print("*"*n)

	
>>> frame(6,10)
******
*    *
*    *
*    *
*    *
*    *
*    *
*    *
*    *
******
>>> frame(14,3)
**************
*            *
**************
>>> path = "/Users/mac365.vn/documents/kaikki/python/"
>>> fh = open(path +"react.txt","a")
>>> import re
>>> import string
>>> frequency = {}
>>> text = fh.read().lower()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    text = fh.read().lower()
io.UnsupportedOperation: not readable
>>> fh = open(path +"react.txt","r")
>>> text = fh.read().lower()
>>> pattern = re.findall(r'\b[a-z]{3,15}\b', text)
>>> for word in pattern:
	count = frequency.get(word,0)
	frequency[word] = count +1

	
>>> frequency_list=  frequency.keys()
>>> for word in frequency_list:
	print(word + " "*(12 -len(word)) + frequency[word])

	
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(word + " "*(12 -len(word)) + frequency[word])
TypeError: can only concatenate str (not "int") to str
>>> " " * len("hello")
'     '
>>> " " * (12-len("h"))
'           '
>>> for word in frequency_list:
	print(word," "*(12 -len(word)), frequency[word])

	
react         13
computing     1
also          1
known         1
reactjs       1
javascript    1
library       2
for           4
building      2
user          2
interfaces    2
maintained    1
facebook      5
and           7
community     1
individual    1
developers    1
companies     1
can           1
used          1
base          1
the           4
development   3
single        1
page          1
mobile        1
applications  2
complex       1
usually       1
require       1
use           1
additional    1
libraries     1
state         1
management    1
routing       1
interaction   1
with          2
api           1
was           6
created       1
jordan        1
walke         1
software      1
engineer      1
influenced    1
xhp           1
html          1
component     1
framework     3
php           1
first         1
deployed      1
newsfeed      1
later         1
instagram     1
com           1
open          2
sourced       2
jsconf        1
may           1
native        2
which         1
enables       1
android       1
ios           1
uwp           1
announced     2
conf          1
february      1
march         1
april         1
fiber         2
new           1
core          1
algorithm     1
become        1
foundation    1
any           1
future        1
improvements  1
feature       1
>>> #exercise4
>>> morse = {'a': '*-', 'A': '*-', 'b': '-***', 'B': '-***', 'c': '-*-*',
         'C': '-*-*', 'd': '-**', 'D': '-**',
         'e': '*', 'E': '*', 'f': '**-*', 'F': '**-*', 'g': '--*',
         'G': '--*', 'h': '****', 'H': '****',
         'i': '**', 'I': '**', 'j': '*---', 'J': '*---',
         'k': '-*-', 'K': '-*-', 'l': '*-**', 'L': '*-**',
         'm': '--', 'M': '--', 'n': '-*', 'N': '-*',
         'o': '---', 'O': '---', 'p': '*--*', 'P': '*--*',
         'q': '--*-', 'Q': '--*-', 'r': '*-*', 'R': '*-*',
         's': '***', 'S': '***', 't': '-', 'T': '-',
         'u': '**-', 'U': '**-', 'v': '***-', 'V': '***-',
         'w': '*--', 'W': '*--', 'x': '-**-', 'X': '-**-',
         'y': '-*--', 'Y': '-*--', 'z': '--**', 'Z': '--**',
         '0': '-----', '1': '*----', '2': '**---', '3': '***--', '4': '****-',
         '5': '*****', '6': '-****', '7': '--***', '8': '---**', '9': '----*',
         '.': '*-*-*-', ',': '--**--', '?': '**--**', ' ': '   '}

>>> def Morse():
	text = input("Give short text: ")
	for f in text:
		print(morse[f] + " ")

>>> Morse()
Give short text: Finland
**-* 
** 
-* 
*-** 
*- 
-* 
-** 
>>> Morse()
Give short text: Truc Anh
- 
*-* 
**- 
-*-* 
    
*- 
-* 
**** 
>>> 
