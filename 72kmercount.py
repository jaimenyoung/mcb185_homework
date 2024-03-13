import sys
import mcb185
import itertools

#cl: python3 72kmercount.py ecoli.fna.gz 2

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1                           #incr counts of each observed kmer
for kmer, n in kcount.items(): print(kmer, n)

#cl: python3 72kmercount.py ecoli.fna.gz 7 | sort -nk2 | head

#reports all possible kmers
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)
