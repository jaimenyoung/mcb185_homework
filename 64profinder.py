# Input: multi-FASTA file of DNA
# Output: multi-FASTA file of proteins
# Must perform a six-frame translation
# Proteins must be at least 100 amino acids long
# Proteins must start with 'M' and end with '*'
# Deflines must have unique identifiers

# cl: python3 64profinder.py ecoli.fna.gz 100

import dogma
import mcb185
import sys

file = sys.argv[1]
min_length = int(sys.argv[2])

def profinder(seq, min_length):
	proteins = []
	for frame in dogma.translate(seq).split('*'):
		if 'M' in frame:
			search = frame.find('M')
			aa_seq = frame[search:]
			if len(aa_seq) >= min_length:
				proteins.append(aa_seq + '*')
	return proteins

aa_count = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	pos_prot = profinder(seq, min_length)
	neg_prot = profinder(dogma.revcomp(seq), min_length)
	for frame in range(3):
		for pos in pos_prot:
			aa_count += 1
			print(f'>{defwords[0]}-prot-{aa_count}\n{pos}')
		for neg in neg_prot:
			aa_count += 1
			print(f'>{defwords[0]}-prot-{aa_count}\n{neg}')
