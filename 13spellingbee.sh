#Authors: Jaime Young, Madison An
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ."{4,}" 

