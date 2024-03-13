#IN CLASS
'''
import random
random.seed(1)     #gives you same random sequence every time

#random words (token)
size = 1000
#words = []
wordd = {}
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
	#words.append(token)
	wordd[token] = True

for i in range(1000):
	if 'MYNAMEISIAN' in word:           #in
		print('found')
	

n       'in'        'dict'
1e4     0.195s     0.091
1e5     1.667s     0.56
1e6     16.318s    5.358

#dictionary is faster



#first demo way

def kdh_stack(seq): 
	kds = 0
	for aa in seq:
		if   aa == 'I': kds +=(4.5)
		elif aa == 'V': kds +=(4.2)
		elif aa == 'L': kds +=(3.8)
		elif aa == 'F': kds +=(2.8)
		elif aa == 'C': kds +=(2.5)
		elif aa == 'M': kds +=(1.9)
		elif aa == 'A': kds +=(1.8)
		elif aa == 'G': kds +=(-0.4)
		elif aa == 'T': kds +=(-0.7)
		elif aa == 'S': kds +=(-0.8)
		elif aa == 'W': kds +=(-0.9)     #add value to list
		elif aa == 'Y': kds +=(-1.3)
		elif aa == 'P': kds +=(-1.6)
		elif aa == 'H': kds +=(-3.2)
		elif aa == 'E': kds +=(-3.5)
		elif aa == 'Q': kds +=(-3.5)
		elif aa == 'D': kds +=(-3.5)
		elif aa == 'N': kds +=(-3.5)
		elif aa == 'K': kds +=(-3.9)
		elif aa == 'R': kds +=(-4.5)
	return kds / len(seq)


#make a random protein
protein_length = 300
protein = []
for i in range(protein_length):
aa = random.protein('ACDEFGHIKLMNPQRSTVWY')
	protein.append(aa)
protein = ''.join(protein)
print(protein)


for i in range 10000:
	sumh = 0
	for aa in protein:
		sumh += kdh(aa)
	#print(sumh/protein_length)

for i in range(2):
	kdh_stack(protein)



#list variant
	def kdh_list(seq):
	kdsum = 0
		aas = 'IVLFCMAGTSWYPHEQDNKR'         #parallel lists
		kds = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5, 0)
	for aa in seq:
		idx = aas.index(aa)
		kd = kds[idx]
		kdsum += kds[idx]
	return kdsum / len(seq)

for i in range(1000):
	print(kdh_list(protein))

#dictionary -paired letter and numbers


KDT = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5}


def kdh_dict(seq):
	kdsum = 0
	for aa in seq:
		if aa in KDT: kdsum += KDT[aa]  #if aa in dict, add.
	return kdsum / len(seq)

for i in range(1000):
	print(kdh_dict(protein))
'''
#dictionaries for categorizing(growing unique list) and fast lookups
'''

import mcb185
import sys
import itertools

kcount = {}
k = 3
for aas in itertools.product('ACDEFGHIKLMNPQRSTVWY', repeat = 3)
	kmer = ''.join(aas)
	kcount[kmer] = 0
	#print(aas)        #all possible combos of aas
	
for kmer, n in kcount.items():
	print(kmer, n)
	
for defline, seq in mcb1885.read_fasta(sys.argv[1])
	#print(seq[:30]) #print first 30 aa
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		print(kmer)
		if kmer not in kcount: kcount[kmer] = 0    #makes count if not already made
		kcount[kmer] += 1

for kmer, n in kcount.items():
	print(kmer, n)         #counts for kmer aa combos
'''


#DEMO

#DICTIONARY BASICS
d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

#add to dictionary
d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

#ITERATION
#for loop in order of creation

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)      #most common, tuples unpacked

print(d.keys(), d.values(), list(d.values()))

#LOOKUP TABLES

kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M':  1.9, 'A':  1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)


#COMPOSITION AGAIN
'''
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
'''
#SORTING-- see  71countgff.py
#sorting by value with lambda:
'''
def by_value(tuple):
	return tuple[1]
	
for k, v in sorted(count.items(), key=by_value):   #calls by_value function on each tuple to get the thing used for sorting(the value)
	print(k,v)
'''

#ITERTOOLS

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)




























