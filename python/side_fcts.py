import re

def is_all_float(arg):
	try:
		float(arg)
		return True
	except ValueError:
		return False

def is_all_int(arg):
	try:
		int(arg)
		return True
	except ValueError:
		return False

def occ_count(pattern, string, ct=0):
	a = re.findall(pattern, string)
	print (a)
	while ct < len(a):
		ct += 1
	return ct
