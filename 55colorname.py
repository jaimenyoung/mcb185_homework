# 55colorname.py

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
	
def dtc(n):
	r = abs(int(R) - int(n[0])) 
	g = abs(int(G) - int(n[1]))
	b = abs(int(B) - int(n[2]))
	return(r + b + g)
	

with open('../MCB185/data/colors_extended.tsv') as fp:
	min_color = ''
	min_distance = (255 * 3) + 1
	for line in fp:
		words = line.split('\t')
		if words[2]:
			num = words[2].split(',')
			distance = dtc(num)
			if distance < min_distance:
				min_distance = distance
				min_color = words[0]

	print(min_color)