# dc of 5, 10, 15
# probabilty of success with normal, adv, and disadv

import random

def normal():
	r = random.randint(1, 20)
	return r

def advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2: 
		return r1
	else: 
		return r2

def disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 <= r2:
		return r1
	else: 
		return r2

print('DC \tnorm \t adv \tdisadv')

rolls = 10
for dc in range(5, 16, 5):
	print(dc, end='\t')
	nsuccess = 0
	asuccess = 0
	dsuccess = 0
	for i in range(rolls):
	
		norm = normal()
		if norm >= dc:
			nsuccess += 1
		n = nsuccess / rolls
		
		adv = advantage()
		if adv >= dc: 
			asuccess += 1
		a = asuccess / rolls
		
		disadv = disadvantage()
		if disadv >= dc: 
			dsuccess += 1
		d = dsuccess / rolls
		
	print(n, '\t', a, '\t', d)