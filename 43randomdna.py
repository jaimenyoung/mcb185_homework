# Random DNA

import random

nts = 0
seq = 100                       # number of sequences
for i in range(seq):
	print()
	print(f'>seq-{i+1}')
	r = random.randint(50, 60)
	for nts in range(r):
		print(random.choice('ACGT'), end='')
print()