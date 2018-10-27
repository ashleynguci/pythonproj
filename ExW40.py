Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def get_middle():
	s = input('Give me a word: ')
	length = len(s)
	if length % 2 != 0:
		result = s[length// 2]
	else:
		result = s[(length-1)//2] + s[length//2]
	return result
	print("The middle char is ",result)

	
>>> get_middle()
Give me a word: I dont know
't'
>>> def ConvertCtoF():
	a = int(input('Min: ?'))
	b = int(input('Max: ?'))
	for  x in range(a, b+1):
		y = x*9/5 +32
		print(x,y)

		
>>> ConvertCtoF()
Min: ?20
Max: ?29
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
>>> def Chicken():
	cow_leg = [4*cow for cow in range(1, 66)]
	chicken_leg = [2*(65 - cow) for cow in range(1, 66)]
	combine =  [(x,y) for x in cow_leg for y in chicken_leg if x+y ==226 and x/4 ==65-(y/2)]
	chic = [i[1]/2 for i in combine]
	print("Number of chicken is ",chic)

	
>>> Chicken()
Number of chicken is  [17.0]
>>> def Checksum():
    	ref = input("WHHWHWH: ")
    	multi = [7,3,1]
    	index = 0
    	for x in range (0, len(ref)):
    		x = int(len(ref)-1)
    		if index ==3:
    			index ==0
    		sum = int(ref[x]*multi[0]
    		x -=1
             index +=1
        return sum
    print(Checksum())
			  
SyntaxError: invalid syntax
>>> 
