# Random Pi using monte carlo

import math
import random


def distance(x1, y1, x2, y2):
	d = (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
	return d

i = 0
inside = 0
while True: 
	i = i + 1
	x = random.random()
	y = random.random()
	r = distance(x, y, 0, 0)
	if r < 1: inside += 1
	pi = 4 * inside / i
	print(pi)
