#Authors: Jaime Young and Madison An

Jaime Young
jaimenyoung

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsvwxyz]" | grep -E ."{4,}" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsvwxyz]" | grep -E ."{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[cdefghjkmopqsuvwxyz]" | grep -E ."{4,}" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[cdefghjkmopqsuvwxyz]" | grep -E ."{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v "[befghjklpqrstuvwxyz]" | grep -E ."{4,}" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v "[befghjklpqrstuvwxyz]" | grep -E ."{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v "[bcdefhjklmpqstuvwxyz]" | grep -E ."{4,}" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v "[bcdefhjklmpqstuvwxyz]" | grep -E ."{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "diatoms"|grep "diatoms" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "urochordates" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "nematodes" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "fungi" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "insects" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "plants" |wc -l
gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz |grep "vertebrates" |wc -l

