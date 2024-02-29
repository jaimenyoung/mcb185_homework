#a hydrophobic signal peptide near the N-terminus
#other hydrophobic regions to cross the plasma membrane

#Looking for:
#signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
#transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
#no prolines in either hydrophobic region


import sys
import mcb185
import dogma

#signal peptide: 8 aa long, average KD >= 2.5, first 30 aa, no proline


#cl: python3 65transmembrane.py ecoliprot.faa.gz




#seq = 'MVLIVLCICLVCILGAHSRTKGIEALSTREWKMAKETRYGAVLIMPSFLAMEINGVCLVCLVCL'

def sig_pep(seq):
	w = 8
	s = 1
	for i in range(0, len(seq) -w +1, s):      #slide 8 across until 30 aa. 
		if i + w <= 30:
			sp = seq[i:i+w]
			#print(sp)
			hydro_score = dogma.hydropathy(sp) #calc kdh
			#print(hydro_score)
			if hydro_score >= 2.5 and 'P' not in sp:   #if kdh<2.5 and no proline print name
				


def trans_reg(seq):
	w = 11
	s = 1
	for i in range(30, len(seq) -w +1, s):
		tr = seq[i:i+w]
		#print(tr)
		hydro_score = dogma.hydropathy(tr) #calc kdh
		#print(hydro_score)
		if hydro_score >= 2.0 and 'P' not in tr:   #if kdh<2.5 and no proline print name
			

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split(']')
	name = defwords[0]
	if sig_pep(seq) and trans_reg(seq):
		print(name + ']')






