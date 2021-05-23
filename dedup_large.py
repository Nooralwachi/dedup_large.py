import sys
def dedup_large(filename):
	lines= set()	
	lines_gen=(line.strip() for line in open(filename))
	for line in lines_gen:
		if line.strip() not in lines:
			lines.add(line.strip())
	with open('non_duplicates.txt', 'w') as fw:
		for line in lines:
			fw.write(line + '\n')



dedup_large('large.txt')