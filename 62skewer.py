# 62: one letter coming off and on, see if g and c
# drop one letter off and pick up another until at the end (loop)
# update as you go, average of each window

# cl: python3 62skewer.py ecoli.fna.gz 1000

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = int(sys.argv[2])
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		off = seq[i - 1]
		on = seq[i + w - 1]
		#print(off, on)
	
		if i == 0:
			c = s.count('C')
			g = s.count('G')

		else:
			if   off == 'C': c -= 1
			elif off == 'G': g -= 1
	
			if   on == 'C': c += 1
			elif on == 'G': g += 1
	
		comp = (g+c) / w
		if (g + c) > 0: skew = (g-c) / (g+c)
		else:           skew = 0
		
		print(f'{i}\t{comp:.3f}\t{skew:.3f}')
