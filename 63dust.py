# Input: multi-FASTA file of DNA
# Output: multi-FASTA file of DNA with low complexity regions masked
# Change all low-complexity regions to 'N' in the output
# Provide parameters for fasta file, window size, and entropy

#cl:  python3 63dust.py ecoli.fna.gz 20 1.4

import math
import sys
import mcb185

def nt_counts(seq):
	A = 0
	C = 0
	G = 0
	T = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
	
	return A, C, G, T
	
	
def entropy(a, c, g, t): 
	total = (a + c + g + t)
	
	xa = a / total
	xc = c / total
	xg = g / total
	xt = t / total
	
	if   a != 0: ha = xa * math.log2(1 / xa)
	elif a == 0: ha = 0
	
	if   c != 0: hc = xc * math.log2(1 / xc)
	elif c == 0: hc = 0
	
	if   g != 0: hg = xg * math.log2(1 / xg)
	elif g == 0: hg = 0
	
	if   t != 0: ht = xt * math.log2(1 / xt)
	elif t == 0: ht = 0
	
	return ha + hc + hg + ht


dnafile = sys.argv[1]
w = int(sys.argv[2])            #20
ent_thres = float(sys.argv[3])  #1.4

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	dust_seq = list(seq)
	for i in range(0, len(seq) -w +1):
		window = seq[i:i+w]
		A, C, G, T = nt_counts(window)
		ent = entropy(A, C, G, T)
		if ent < ent_thres:
			for j in range(i, i + w):
				dust_seq[j] = 'N'
	print(defline)
	print( ''.join(dust_seq))
	
