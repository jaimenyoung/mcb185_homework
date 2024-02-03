# function that solves n! / k!(n-k)!

def factorial(n):
	f = 1
	for i in range(1, n + 1):
		f = f * i
	return(f)

def nchoosek(n, k):
	fn = factorial(n)
	fk = factorial(k)
	fnk = factorial(n - k)
	return fn / (fk * fnk)
	
print(nchoosek(4, 2))