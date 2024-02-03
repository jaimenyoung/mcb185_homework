i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)



for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)
	
for i in range(5):              #starts at 0, so no need to do (0,5)
	print(i)
 
for i in range(0, 5, 1):        # 1= step by 1 --for example, codons would step by 3
	print(i)
	
for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)
	
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
	
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
		
limit = 4
for i in range(0, limit):
	for j in range(i+1, limit):
		print(i+1, j+1)
		
#Algorithms

def gc_comp(seq):
	gc_count = 0                        #initialization (setting)
	total = 0
	for nt in seq:                      #iteration (loop over nucleotides of the sequence)
		if nt == 'C' or nt == 'G':      # gc_count only incr if C or G, but all nt must b counted
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total             #finalization
	
print(gc_comp('ACAGCGAAT'))
		
		
		
#PRACTICE

# function that calculates triangular number (sum of numbers from 1 to n)

def triangle(a):
	total = 0               #initialize at 0
	for i in range(a + 1):  
		total = total + i   #each iteration adds to the current value of the loop variable
	return total                  #total = 0 + i
	
print(triangle(4))

# function calculating factorial of a number


def factorial(a):
	total = 1                     #initialize at 1, since can't at 0 for factorials
	for i in range(1, a + 1):     
		total = total * i
	return total
	
print(factorial(4))

# estimates Euler's numbers

def euler(a):
	total = 0
	for i in range(a):                    #loops i for factorial
		total = total + 1 / factorial(i)
	return total
	
print(euler(100))

# perfect square?

import math

def perfect_square(a):
	root = math.sqrt(a)            #line 110: mathclose compares the numbers, // makes it a rounded integer.
	if math.isclose(root, root // 1): return 'perfect square'
	else: return 'false'          # else statement not necessary
	
print(perfect_square(4))

# is number an integer?
	
	
# prime number?

def prime(a):
	for i in range(2, a // 2):
		if a % i == 0: return False
	return True
		
print(prime(6))
print(prime(2))

#divisible by any of the numbers below it?
		
		
		
		
		
		
		
		
		
		