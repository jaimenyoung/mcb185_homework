# generates DNA in FASTA format
# variable controlling how many sequences and identifier
# length is random (50-60)

import random

nts = 0
seq = 101                         # number of sequences
for i in range(1, seq):                  # how to delete space?
	print()
	print(f'>seq-{i}')
	r = random.randint(50, 60)
	for nts in range(r):
		print(random.choice('ACGT'), end='')
print()