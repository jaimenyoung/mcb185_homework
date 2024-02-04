# poisson probability

import math

def factorial(n):
	f = 1
	for i in range(1, n + 1):
		f = f * i
	return f
	
def poisson(n, k):
	return((n ** k) * (math.e ** -n)) / factorial(k)
	
print(poisson(2, 3))
print(poisson(7, 10))
print(poisson(3, 0))

