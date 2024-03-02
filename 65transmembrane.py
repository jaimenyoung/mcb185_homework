# looking for:
# signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
# transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
# no prolines in either hydrophobic region

#cl: python3 65transmembrane.py ecoliprot.faa.gz

import sys
import mcb185
import dogma


def transmem(seq, w, t):
	for i in range(len(seq) -w +1):
		tm = seq[i:i+w]
		hydro_score = dogma.hydropathy(tm)
		if hydro_score >= t and 'P' not in tm:
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split(']')
	name = defwords[0]
	if transmem(seq[:30], 8, 2.5) and transmem(seq[30:], 11, 2.0):
		print(name + ']')
