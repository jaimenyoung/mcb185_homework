
import random

#python3 42chicago.py | sort -n |uniq -c | sort -nk2

zerogame = 0
gamesplayed = 10000
totalscore = 0
for i in range(gamesplayed):             # number of games
	score = 0
	for roundnum in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnum:
			score += roundnum
	
	totalscore += score
	if score == 0:
		zerogame += 1
		
print(zerogame / gamesplayed)
print(totalscore / gamesplayed)


import random

games = 10
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target}')

import random 
import sys

games = 1000000 
log = games // 100                          # report progress at 1% intervals
total = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1
	total += score
print('average score =', total / games)
print('% games with score of 0 =', zeroes / games)

