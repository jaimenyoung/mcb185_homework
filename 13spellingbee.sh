gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep "[zoncai]" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ."{4,100}"
