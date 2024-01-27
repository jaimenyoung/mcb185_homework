#Entropy

import math

def entropy(a, c, g, t): 
	total = (a + c + g + t)
	
	xa = a / total
	xc = c / total			#frequency of nucleotide/total
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
		

print(entropy(2, 3, 1, 0))
print(entropy(9, 12, 3, 4))
print(entropy(0, 4, 0, 18))