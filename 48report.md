Unit 4 Report
=============

45: DnD Stats
+ Reports average stats using the rules below:
  + 3D6: roll 3 six-sided dice
  + 3D6r1: roll 3 six-sided dice, but re-roll any 1s
  + 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
  + 4D6d1: roll 4 six-sided dice, dropping the lowest die roll



46: Saving Throws
+ Reports saving throws for difficulty class (DC) 5, 10, and 15 with an advantage
  disadvantage, and normally.
  + Normal: need to roll higher than the DC
  + Advantage: roll 2 die, choose the higher roll
  + Disadvantage: roll 2 die, choose the lower roll
  
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

47: Death Saves
+ Reports probability one dies, survives, or is revived through simulated death saves
