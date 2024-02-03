# pythagorean triples

# is the hypotenuse an integer or not?
# try 1-100 combos for two sides of the triangle, then see if hypot is an integer

#write loop inside of loop to get combos of numbers
		
import math
limit = 100
for i in range(1, limit):
	for j in range(i, limit):
		c = (i**2 + j**2) ** 0.5
		if math.isclose(c, c // 1):
			print(i, j, c)
		