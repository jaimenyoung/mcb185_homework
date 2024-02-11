# generates numbers from normal dis and calculate how many
# z scores above the mean

import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)       #each iteration needs a random number
	if r > 1: z1 += 1
	if r > 2: z2 += 2                #several variables keep track of z
	if r > 3: z3 += 3
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)



















'''

import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000
	for i in range(limit)
		r = random.gauss(0.0, 1.0)
		if r > 1: z1 += 1
		if r > 2: z2 += 2
		if r > 3: z3 += 3
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)

'''