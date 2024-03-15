'''
import sys
print(sys.argv)
print(sys.argv[1][2])



things = []
things.append('milk')
things.append('cookies')
print(things[0][2])


#2DIMENSIONAL DATA, list in list
matrix = [
	[1, 2, 3], 
	[4, 5, 6]
	[7, 8, 9],
]

print(matrix)
print(matrix[2][0])

import json
person = {
	'name': 'Jaime',
	'age': '20',
	'weight': '0',
	'pets': ['Kodie', 'Sadie'],
	'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad',
	}
}

people = []
people.append(person)
print(json.dumps(person, intent=4))
people[0]['made this up'] = 'hello'
poeple[0]['mentees']['Ismael'] = 'grad'
people[0]['pets'].append('Fizzbuzz')
print(people[0]['mentees']['Claire'])         #undergrad
'''
'''
#cl: python3 80demo.py ~/Code/MCB185/data/C.elegans.fa.gz 4

import json
import mcb185
import sys

k = int(sys.argv[2])
kloc = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kloc: kloc[kmer] = {}
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = []
		kloc[kmer][chrom].append(i)

print(json.dumps(kloc, indent = 4))

	
	
#for 82- read file, create data structire, list of dictionaries
#83- get translation start site from genbank file(gbff) 
#get seq into sequence variable to pull out seq around ATGs


'''
import sys

print(sys.argv)
print(sys.argv[0][3])

d = [
	'hello',
	(3.14, 'pi'),
	[-1, 0, 1],
	{'year': 2000, 'month': 7}
]

print(d[0][4], d[1][0], d[2][2], d[3]['month'])

oligo = {
	'Name': 'S0116',
	'Length': 18,
	'Sequence': 'ATTTAGGTGACACTATAG',
	'Description': 'SP6 promotor sequencing primer'
}

catalog = []
catalog.append(oligo)

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
		return catalog

catalog = read_catalog('../MCB185/data/primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
	
###
'''
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

def oligo(seq):
	A, C, G, T = nt_counts(seq)
	o = A + C + G + T
	
	if o <= 13:
		return(A + T)*2 + (G + C)*4
		
	elif o > 13:
		return 64.9 + 41*(G + C - 16.4) / o
		
		
import dogma

for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)
'''

#DICT OF LISTS

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)


# COMPLEX DATA, JSON

import json 

truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'}, 
	'numbers': [1.09, 3.72, 3.14],
	'is_complete': False,
}

print(json.dumps(truc, indent=4))

# REGULAR EXPRESSIONS


#introns by find , get seq 























