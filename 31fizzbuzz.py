# divisible by 3 = fizz
# divisible by 5 = buzz
# divisible by 3 and 5 = fizzbuzz

for i in range(1,101):
	if i % 3 == 0:
		print('fizz')
	if i % 5 == 0:
		print('buzz')
	if i % 15 == 0:
		print('fizzbuzz')
	else: print(i)