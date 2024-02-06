# Authors: Jaime Young and Madison An


def gregory(n):
	a = 0
	e = 1
	f = 0
	for pi in range(n):
		pi = 1 + f
		a = a + 2
		d = e / a
		e = e * (-1)
		f = f + d
	return (pi * 4)

print(gregory(100))
