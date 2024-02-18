'''
seq = 'GAATC'
print(seq[0], seq [1])
print(seq[-1])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2]) #[start, end, skip by]

print(s[0:5])           #same
print(s[:5]) 

# (s[0]) == (s[0:1])

print(s[::]) #start at beginning, end at end, go by 1
print(s[::-1]) #going backwards-- good for reverse complement sequences of DNA

print(s, s[::], s[::1], s[::-1])

# Tuples

tax = ('Homo', 'sapiens', 9606)     #construct tuple
print(tax)                          # kind of the same as strings, but with words

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
    
x1, x2 = (quadratic(1, 1, 1))     #better to name variables with 2 first (unpacking tuple)
print(x1)
print(x2)

x= (quadratic(1, 1, 1))     #parenthesis there, it is a tuple
print(x)

print(x[0])          # give you first element of tuple

#Enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):        #prints same thing, but tuple in container
	print(i, nt)
	
for nt in nts:
	print(nt)
	
i = 0
for nt in nts:
	print(i, nt)
	i += 1
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
	print(nt, name)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(nts)):
	print(nts[i], names[i])
	
#lists- like tuples but things inside can be changed
# return from function = tuple
# return list from function if you dont know how long its gonna be. variable length

#53- add numbers to list, how many values, min max. do descritptive stats. appending to list
#get exon thru sort, collect in list and make average



#Birthday

#Check previous to new in row, dont need to go farther than finding one match
#collect month in list and check with each other
#figure out if duplicates in list by checking down list without comparing to self and prev
        #check with half matrix minus major diagonal!!
#gather bday and do matrix or sort and look for duplicates or check as you go 
#check as u go: check new one against everyone else until match (bday is list)

#collect bdays in list: bucket search-- tally marks for month/day, when two in one bucket, end.
			#calendar is a list of values (calendar is list)
	

'''
#INDEXES
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
#SLICES
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])       #both ABCDE
print(s[5:len(s)], s[5:])  #both FGHIJ

print(s, s[::], s[::1], s[::-1])


#TUPLES
tax = ('Homo', 'sapiens', 9606)       #construct tuple
print(tax)                            #note the parenthesis in the output

#cannot change contents of tuple

print(tax[0])       #index
print(tax[::-1])    #slice

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2                              #returns a tuple
	
#When calling function that returns a tuple, either unpack tuple 
#into separate variables or capture entire tuple as single valie
#and access its contents with interior indicies. (ALWAYS UNPACK TUPLE)

x1, x2 = quadratic(5, 6, 1)         #unpacked tuple - yes
print(x1, x2)

intercepts = quadratic(5, 6, 1)     #packed tuple - no
print(intercepts[0], intercepts[1])

#ENUMERATE() AND ZIP() -- numbering and 2 containers
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):         #enumerate - provides index and value in separate variables
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, names in zip(nts, names):    #zip - retrive from 2 containers, return as tuple
	print(nt, names)

for i, (nt, name) in enumerate(zip(nts, names)):    #enumerate the zip
	print(i, nt, name)

#LISTS
nts = ['A', 'T', 'C']     #lists made with []
print(nts)
nts[2] = 'G'              #contents mutable
print(nts)

nts.append('C')           #can add stuff to end of list
print(nts)

last = nts.pop()          #remove items from end of list
print(last)

nts.sort()                #elements of list must be same (ints and floats, but not with strings)
print(nts)
nts.sort(reverse=True)
print(nts)

#new variable for a list is another name for same list (not a copy)

nucleotides = nts         #modifications happen to nts and nucleotides
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

#if you want to make a copy, use list.copy()

#LIST()
items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVW'
print(alph)
aas = list(alph)            #coerce iterables into lists (string into letters)
print(aas)

#SPLIT() AND JOIN() -- splits strings into lists of strings
text = 'good day   to you'    #any spaces = split
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))        #comma becomes delimiter

s = '-'.join(aas)             #lists can turn into strings by join with delimiter
print(s)
s = ''.join(aas)
print(s)

#SEARCHING
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))     #returns index if found
#print('index Z?', alph. index('Z'))   #cant find = error

print('find G?', alph.find('G'))       #only works in strings, not tuple or list
print('find Z?', alph. find('Z'))      #return -1 if cant be found

#if thing in list: idx = list.index(thing)      if dont know if element is in list use in



#PRACTICE PROBLEMS

#function returning min of list

vals = [12, 62, 3, 44, 5, 96, 73, 8, 91, 10]

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
print(minimum(vals))

#function returning min and max

def min_max(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
print(min_max(vals))


#function returning mean of list

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total / len(vals)
	
print(mean(vals))

#function computing entropy of prob dist
import math

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
	
print(entropy([0.2, 0.3, 0.5]))

#function computing Kullback-Leibler distance btwn 2 sets of prob dists

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += q *math.log2(p/q)
	return d
	
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)

print(dkl(p1, p2))

























