# program that determines the averages stat value using the rules

# stat is sum of die
# avg 




import random

# 3D6: roll 3 six-sided dice
rolls = 100
stat = 0
for i in range(rolls):                    # roll 10 times
	for j in range(3):                    # roll 3 die
		dice = random.randint(1, 6)
		stat += dice
avg = stat / rolls
print('3D6   avg stat:', avg)

# 3D6r1: roll 3 six-sided dice, but re-roll any 1s

rolls = 100
r1stat = 0
for i in range(rolls):
	for j in range(3):
		r1dice = random.randint(1, 6)
		if r1dice == 1: 
			r1dice = random.randint(1, 6)
		r1stat += r1dice
r1avg = r1stat / rolls
print('3D6r1 avg stat:', r1avg)


# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
rolls = 100
x2stat = 0
for i in range(rolls):
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2:
			x2stat += d1
		if d2 > d1:
			x2stat += d2
x2avg = x2stat / rolls
print('3D6x2 avg stat:', x2avg)


# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
rolls = 1000
total = 0
for i in range(rolls):
	d1stat = 0
	for j in range(1):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
	
		lowest = d1
		if d2 < lowest: lowest = d2
		if d3 < lowest: lowest = d3
		if d4 < lowest: lowest = d4
	
		if d1 != lowest: d1stat += d1
		if d2 != lowest: d1stat += d2
		if d3 != lowest: d1stat += d3
		if d4 != lowest: d1stat += d4
		total += d1stat
		
print('4D6d1 avg stat:', total / rolls)
		



