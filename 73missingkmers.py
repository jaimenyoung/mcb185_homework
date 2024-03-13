
#Start k at 1 and increase until there are missing k-mers
#Only report the k-mers that are missing
#Stop after finding a value of k with missing k-mers
#Search both strands of the sequence
#The output of your program should find 52 missing k-mers in the E.coli genome at k=8.

#cl: python3 73missingkmers.py ecoli.fna.gz


import mcb185
import sys
import itertools
import dogma


file = sys.argv[1]

missing = True
k = 1
while missing == True:
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		
		for i in range(len(seq) -k +1):
			pos_kmer = seq[i:i+k]
			if pos_kmer not in kcount: kcount[pos_kmer] = 0
			kcount[pos_kmer] += 1
	
		neg = dogma.revcomp(seq)
		for i in range(len(neg) -k +1):
			neg_kmer = neg[i:i+k]
			if neg_kmer not in kcount: kcount[neg_kmer] = 0
			kcount[neg_kmer] += 1 
		
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount: 
			missing = False
			print(kmer)
	k += 1
print(f'k = {k-1}')