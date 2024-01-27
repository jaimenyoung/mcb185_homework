#Oligo Temperature

def oligo(A, C, G, T):
	o = A + C + G + T
	
	if o <= 13:
		return (A + T)*2 + (G + C)*4
		
	elif o > 13:
		return 64.9 + 41*(G + C - 16.4) / o
	
	
print(oligo(2, 4, 3, 5))
print(oligo(12, 65, 9, 15))

