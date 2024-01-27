# 20demo.py by Jaime Young

print('hello, again')

import math

print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))

print(abs(-11))
print(pow(3, 2))
print(round(4.567, ndigits=1))

print(math.ceil(23.4567))
print(math.floor(1.843998))
print(math.log(2))
print(math.log2(3))
print(math.log10(1000))
print(math.sqrt(100))
print(math.pow(4, 3))
print(math.factorial(5))

print(math.e)
print(math.pi)
print(math.inf)
print(math.nan)

print(0.1 * 1)
print(0.1 * 3)

a = 3							# side of triangle
b = 4							# side of triangle
c = math.sqrt(a**2 + b**2)		# hypotenuse 
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=',')

def greeting():
	print('hello yourself')
	
def pythagoras (a, b):
	c = math.sqrt(a**2 + b**2)
	return c
	
x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))
print(pythagoras(1, 1))

#def pythagoras(a, b):
#	assert(a > 0)
#	assert(b > 0)
#	return math.sqrt(a**2 + b**2)
										# ends in error

#def pythagoras(a, b):
#	if a <= 0: sys.exit('error: a must be greater than 0')
#	if b <= 0: sys.exit('error: b must be greater than 0')
#	return math.sqrt(a**2+b**2)
#print (pythagoras(-1, 1))



#practice

#turn neg to pos and vis versa
def pos(a):
	return (-(a))
print (pos(-4))


#compute area, circumference, volume
#Area of Square/Rectangle
def area(a, b):
	return (a * b)
print (area(3, 4))												 #test

#Area of Circle
def area(r):
	return ((math.pi) * (r ** 2))
print (area(3))													 #test

#convert temperature C -> F
def temp(c):
	return ((c * 9/5) + 32)
print (temp(24))												 #test

#convert temperature F -> C
def temp(f):
	return ((f - 32) * 5/9)
print (temp(60))												 #test

#convert speed kph -> mph
def speed(k):
	return (k / 1.609)
print (speed(100))												 #test

#convert speed mph -> kph
def speed(m):
	return (m * 1.609)
print (speed(100))												 #test

#compute DNA conc from OD260 (dsDNA)
def conc(o):
	return (o * 50)
print (conc(2))													 #test

#compute distance between points on a graph
def dist(x1, x2, y1, y2):
	return (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
print (dist(2,3,8,5))											 #test

#compute midpoint
def midpoint (x1, x2, y1, y2):
	return (((x1+x2)/2), ((y1+y2)/2))
print (midpoint (2, 3, 4, 5))									 #test


#Strings
s = 'hello world'
print(s, type(s))


#Conditionals
a = 2
b = 3
if a == b:
	print ('a equals b')
	
if a == b:
	print ('a equals b')
	print(a, b)

if a == b:
	print ('a equals b')
print (a, b)

c = a == b
print(c)
print(type(c))

if a < b:
	print ('a < b')
elif a > b:								#elif: "if the previous conditions not true, try this one"
	print('a > b')
else:
	print('a == b')
	
if    a < b: print ('a < b')
elif  a > b: print ('a > b')
else: print ('a == b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

#Floating Point Warning
a = 0.3
b = 0.1 * 3
if    a < b: print('a < b')
elif  a > b: print('a > b')
else: print ('a == b')

print (abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')


#String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#Mismatched Type Error
#	a = 1
#	s = 'G'
#	if a < s: print('a < s')		Type Error


#PRACTICE
#function that determines if integer
#def isinteger(a):
#	return (type(a))
#print (isinteger(2))

#Odd number

#molecular weight of DNA letter

#complement of DNA letter
nt = A
if   nt == A: print('T')		#doesnt work now
elif nt == T: print('A')	
elif nt == C: print('G')	
elif nt == G: print('C')



	

	
