# pythagorean triples

import math
limit = 100
for i in range(1, limit):
	for j in range(i, limit):
		c = (i**2 + j**2) ** 0.5
		if math.isclose(c, c // 1):
			print(i, j, c)
		