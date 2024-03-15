#cl: python3 84splicesites.py ../MCB185/data/C.elegans.fa.gz ../MCB185/data/C.elegans.gff.gz

import sys
import gzip
import mcb185
import json

fasta = sys.argv[1]
gff = sys.argv[2]

def print_pwm(pwm, acc, id, de):
	print('AC', acc)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('PO      A       C       G       T')
	for i, d in enumerate(pwm):
		print(i+1, end='\t')
		for nt, n in d.items():
			print(n, end='\t')
		print()
	print('XX')
	print('//')

# read all sequences
chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chid = defline.split()[0]
	chrom[chid] = seq

# read all features (introns)
introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]                # chromosome
		t = f[2]                # type
		b = int(f[3]) - 1       # beg
		e = int(f[4]) - 1       # end
		n = f[5]                # number
		s = f[6]                # strand
		if t != 'intron': continue
		if n == '.': continue
		n = float(n)
		introns.append( (c, b, e, n, s) )

# initialize pwms
don = []
for i in range(6):
	don.append( {'A': 0, 'C': 0, 'G': 0, 'T': 0} )
acc = []
for i in range(7):
	acc.append( {'A': 0, 'C': 0, 'G': 0, 'T': 0} )
	
# get all sequences of splice site
for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b:e+1]
		#print(iseq[0:2], iseq[-2:])      #follows gtag rule
	else:
		iseq = mcb185.anti_seq(chrom[c][b:e+1])     #reverse comp
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] += 1
	aseq = iseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += 1

print_pwm(acc, 'DEMO1', 'ACC', 'splice acceptor')
print_pwm(don, 'DEMO2', 'DON', 'splice donor')
