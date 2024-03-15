#Authors: Jaime Young and Avery Adelseck
#cl: python3 74genefinder.py ecoli.fna.gz 300

import sys
import dogma
import mcb185


min_length = int(sys.argv[2])
def genefinder(seq, min_length):
	genes = []
	for frame in range(3):
		fseq = seq[frame:]
		i = 0
		while i < len(seq):
			codon = fseq[i:i+3]
			if codon == 'ATG':
				start = i
			
				for j in range(i, len(fseq) -2, 3):
					codon = fseq[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j
						length = stop - start + 1
						if length >= min_length:
							genes.append((start + frame, stop + frame + 2))
						i = stop
						break
			i += 3
	return genes

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	neg = dogma.revcomp(seq)
	
	pgenes = genefinder(seq, min_length)
	for start, stop in pgenes:
		print(start + 1, stop + 1, '+')

	ngenes = genefinder(neg, min_length)
	for start, stop in ngenes:
		start_neg = len(seq) - stop
		end_neg = len(seq) - start
		print(start_neg, end_neg, '-')

