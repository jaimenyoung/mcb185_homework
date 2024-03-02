# Input: multi-FASTA file of DNA
# Output: multi-FASTA file of proteins
# Must perform a six-frame translation
# Proteins must be at least 100 amino acids long
# Proteins must start with 'M' and end with '*'
# Deflines must have unique identifiers

# cl: python3 64profinder.py ecoli.fna.gz

import dogma
import mcb185
import sys

def profinder(seq):
	start = False
	aa_seq = ''
	#aa_count = 0
	proteins = []
	for frame in range(3):
		for i in range(frame, len(seq)-3 +1, 3):
			codon = seq[i:i+3]
			aa = dogma.translate(codon)
			if aa == 'M':
				start = True
			if start:
				aa_seq += aa
			if aa == '*':
				if len(aa_seq) >= 100:
					#aa_count += 1
					proteins.append(f'{aa_seq}')
				aa_seq = ''
				start = False
	return proteins

aa_count = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	pos_prot = profinder(seq)
	neg_prot = profinder(dogma.revcomp(seq))
	for pos in pos_prot:
		aa_count += 1
		print(f'>{defwords[0]}-prot-{aa_count}\n{pos}')
	for neg in neg_prot:
		aa_count += 1
		print(f'>{defwords[0]}-prot-{aa_count}\n{neg}')
