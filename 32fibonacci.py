# fibonacci
# report first 10 numbers from fibonacci sequence
# initialize and keep track of 2 prev values
# fibo = n = sum of 2 preceding numbers


def fibonacci(n):
	f1 = 0   
	f2 = 1
	print(f1)
	print(f2)
	for i in range(n-2):            # n = number of terms
		f3 = f1 + f2
		print(f3)
		f1 = f2
		f2 = f3
		
print(fibonacci(10))


		




# keep track of previous 2 values
#sum up, then rotate values through
