import gzip
import sys

count = {}                                  #key(feature):  value(freq)
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()                    #retrieve feature name from the line
		feature = f[2]
		if feature not in count: count[feature] = 0    #if feature not in dictionary, create new key
		count[feature] += 1
	for f, n in count.items(): print(f, n)
print()
#cl: python3 71countgff.py ecoli.gff.gz

#sorted by keys:
for k in sorted(count): print(k, count[k])
print()

#sorted by values:
for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)