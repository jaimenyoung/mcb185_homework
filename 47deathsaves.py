#Authors: Jaime Young and Madison An

import random

rolls = 10000
games = 0                  # number complete scenarios
stable = 0                 # scenarios ending in stable
die = 0                    # scenarios ending in die
revived = 0                # scenarios ending in revive

scs_tot = 0                # total success rolls
fail_tot = 0               # total fail rolls
for i in range(rolls):
	revive = 0
	success = 0
	fail = 0
	for j in range(1):
		r = random.randint(1, 20)

		if r == 1: 
			fail += 2
		if r == 20: 
			revive += 1
			games += 1
		if 2 <= r <= 9: 
			fail += 1
		if 10 <= r <= 19: 
			success += 1
			
	scs_tot += success
	fail_tot += fail
	revived += revive
		

	if fail_tot % 3 == 0 and fail > 0: 
		die += 1
		games += 1
	if scs_tot % 3 == 0 and success > 0: 
		stable += 1
		games += 1
	
print('p(die)=', die / games)
print('p(stable)=', stable / games)
print('p(revived)=', revived / games)
		
		
	
		
		
		
		
		
		

