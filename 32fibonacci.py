# fibonacci 

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

