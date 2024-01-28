#Accuracy

import sys

def accuracy(tp, fp, tn, fn):
	if tp == 0: sys.exit('error: tp must be greater than 0')
	
	p = tp / (tp + fp)	
	r = tp / (tp + fn)	
	F1 = (2 * (p*r)) / (p + r)	
	A = (tp + tn) / (tp + fp + tn + fn)	
	
	return F1, A
	

print(accuracy(2, 5, 3, 9))
print(accuracy(0, 2, 5, 0))
print(accuracy(5, 10, 3, 4))