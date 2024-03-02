# 62: one letter coming off and on, see if g and c
# drop one letter off and pick up another until at the end (loop)
# update as you go, average of each window

# cl: python3 62skewer.py ecoli.fna.gz 1000

import sys
import dogma
import mcb185

dnafile = sys.argv[1]
window = sys.argv[2]

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	w = int(sys.argv[2])                 #number nts in window
	s = seq[:w+1]                        #first window sequence
	gc = 0
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]                   #moving window up 1 nt
		if seq[i - 1] == 'G' or 'C':     #leaving window
			gc -= 1
		if seq[w + i - 1] == 'G' or 'C': #entering window
			gc += 1
		print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
		