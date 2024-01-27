#Accuracy

import sys

def accuracy(tp, fp, tn, fn):
	if tp == 0: sys.exit('error: tp must be greater than 0')
	
	p = tp / (tp + fp) 						#precision
	r = tp / (tp + fn)						#recall
	F1 = (2 * (p*r)) / (p + r)         		#F1 score
	A = (tp + tn) / (tp + fp + tn + fn)		#accuracy
	
	return F1, A
	

print(accuracy(2, 5, 3, 9))
print(accuracy(0, 2, 5, 0))