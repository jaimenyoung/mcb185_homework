#47 Death Saves

import random

rolls = 10000
die = 0
stabilize = 0
revive = 0
for i in range(rolls):
	fail = 0
	success = 0
	while True:
		r = random.randint(1, 20)
		if r == 1:
			fail += 2
		elif r == 20:
			revive += 1
			break
		elif 10 <= r <= 19:
			success += 1
		elif 2 <= r <= 9:
			fail += 1
		
		if success == 3:
			stabilize += 1
			break
		elif fail == 3:
			die += 1
			break

total = die + stabilize + revive
prob_die = die / total
prob_stable = stabilize / total
prob_revive = revive / total

print('probability of dying =', prob_die)
print('probability of stabilizing =', prob_stable)
print('probability of reviving =', prob_revive)
		
	
		
		
		
		
		
		

