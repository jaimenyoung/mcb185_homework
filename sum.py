# s = 'j'
# print(ord(s))

'''
def chksum(s):
	n = 0                # sum everything up
	for c in s:
		n = n + ord(c)
	return n % 256      

# get letter with maximum value
# whats max letter ive seen?

def maxchar(s):
	mx = 0                       #initialization
	for c in s:
		if ord(c) > mx: 
			mx = ord(c)          #new maximum
	return mx
	
def minchar(s):
	mn = 300
	for c in s:
		if ord(c) < mn:
			mn = ord(c)
	return mn

import math
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / math.factorial(n)
		print(e)                   #gets closer with each iteration
	return e

def is_perfect_square(n):
	root = math.sqrt(n)
	if root == root // 1: 
		return True
	return False

def is_prime(n):
	for den in range(2, n // 2):           #den is denominator
		if n % den == 0: return False
	return True


name = 'jaime'
print(chksum(name))
print(maxchar(name))
print(minchar(name))
print(euler(10))
print(is_perfect_square(2))
print(is_prime(3))

'''

limit = 5
for i in range(1, limit):
	for j in range(i, limit):           #loop in loop pairs values, but we get same answer twice, so start second loop at current val of 1st loop
		print(i, j, 'c')                  #sides of triangle



# for j in range(limit)         every row and every column  
# for j in range(i, limit)      half matrix with major diagonal
# for j in range(i + 1, limit)  half matrix without major diagonal
# for j in range(i, limit)  full matrix, no major diagonal
#               if i != j:











