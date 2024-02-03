#Authors: Jaime Young and Madison An
		
		
import math
def nilakantha(x):
	n = 2
	pi = 3
	s = 1
	for i in range(x):
		pi = pi + s*(4 / (n * (n + 1) * (n + 2)))
		s = s * (-1)
		n = n + 2
	return pi
		
		
print(nilakantha(100))