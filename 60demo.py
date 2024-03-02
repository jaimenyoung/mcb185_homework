import sys
import mcb185

#calculate gc composition of nucleotide seq in fasta file
'''
#original
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))

#new
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt =='C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
	
#if, elif, else stack
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
	print(A/len(seq), C/len(seq), G/len(seq), T/len(seq), n/len(seq))

#list variation
nts = 'ACGTN'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	counts = []
	name = defwords[0]
	for i in range(len(nts)): counts.append(0)
	for nt in seq:
		if   nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:           counts[4] += 1
	print(name, end='\t')
	for n in counts: print(f'[n/len(seq):.4f]', end='\t')
	print()
'''	
#indexing with str.find()
nts = 'ACGTN'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	counts = [0] * len(nts)        #change all counts to 0
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()
'''

#counting with str.count()
nts = 'ACGTN'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
		
#cl: gunzip -c ~/Code/MCB185/data/A.thaliana.fa.gz | grep -v ">" | grep "[^ACGTN]"

#SLIDING WINDOW ALGORITHM
w = 10    #sets size of window
s = 1     #step size
for i in range(0, len(seq) -w +1, s):      #moves window
	subseq = seq[1:1+w]                    #creates subsequence using offset i and w
	

	
'''

#IN CLASS-- 62skewer.py
seq = 
w = 10
g = seq[0:w].count('G')
c = seq[0:w].count('C')

for i in range(len(seq) -w +1):
	off = seq[i]
	on = seq[i+w]
	print(off, on)
	
	if   off == 'C': c -= 1
	elif off == 'G': g -= 1
	
	if   on == 'C': c += 1
	elif on == 'G': g += 1
	
	comp = (g+c) / w
	if (g + c) > 0: skew = (g-c) / (g+c)
	else:           skew = 0
		
	print(i, comp, skew)




