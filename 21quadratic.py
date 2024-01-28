#Quadratic 

import math

def quadratic(a, b, c):
	d = ((b**2) - (4*a*c)) ** 0.5
	if(b**2) - (4*a*c) > 0:
		x = (-b + d) / (2 * a), (-b - d) / (2 * a)
		return x
	elif(b**2) - (4*a*c) == 0:
		x = (-b + d) / (2 * a)
		return x
	else:
		return 'no real solution'


print(quadratic(1, 5, 6))
print(quadratic(2, 3, 4))
print(quadratic(4, 4, 1))