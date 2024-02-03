#function that computes poisson probability
# (n^k e^-n / k!)

import math

def factorial(n):
	f = 1
	for i in range(1, n + 1):
		f = f * i
	return f
	
def euler(n):
	e = 0
	for i in range(n):
		e = e + 1 / factorial(i)
	return e
	
def poisson(n, k):
	return((n ** k) * (euler(10) ** -n)) / factorial(k)
	
print(poisson(2, 3))
print(poisson(4, 19))
print(poisson(3, 0))

