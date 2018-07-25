import re

def normed_char(s, patt=' +', chr=' '):
	tmp = re.sub(patt, chr, s)
	if tmp:
		s = tmp
		print (s)
		return s
	return s

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

def fraction_shit(s):
	#if re.search('((\d+\.\d+/\d+\.\d+)|(-\d+\.\d+/-\d+\.\d+))|((-\d+\.\d+/\d+\.\d+)|(\d+\.\d+/-\d+\.\d+)|(-\d+/-\d+)|(\d+/\d+)|(-\d+/\d+)|(\d+/-\d+))', s):
	print (s)
	if re.search('-*\d+\.*\d*/-*\d+\.*\d*', s):
		a = re.search('\A-*\d+\.*\d*', s)
		b = re.search('(?<=/)-*\d+\.*\d*(?=\D)', s)
		a = float(a.group())
		b = float(b.group())
		print ('------>', a, b, float(a / b))
		tmp = str(a / b)
		s = re.sub('-*\d+\.*\d*/*-*\d+\.*\d*', tmp, s)
		print ('My floated version', s)
		return s
	print ('Testing')
	return s

def calc_fraction(s):
	print ('Before', s)
	if re.search('(-\d+/-\d+)|(\d+/\d+)|(-\d+/\d+)|(\d+/-\d+)', s):
		a = re.search('(\A\d+)|(\A-\d+)', s)
		b = re.search('(\d+\Z)|(-\d+\Z)', s)
		a = float(a.group())
		b = float(b.group())
		tmp = str(a / b)
		print ('Test 2', tmp, a, b)
		return re.search('(-\d+\.\d+)|(\d+\.\d+)', tmp)
	if re.search('((\d+\.\d+/\d+\.\d+)|(-\d+\.\d+/-\d+\.\d+))|((-\d+\.\d+/\d+\.\d+)|(\d+\.\d+/-\d+\.\d+))', s):
		print ('I m in the decimals')
		a = re.search('\A\d+\.\d+', s)
		b = re.search('\d+\.\d+\Z', s)
		a = float(a.group())
		b = float(b.group())
		tmp = str(a / b)
		print ('Test', tmp, a, b)
		return re.search('(-\d+\.\d+)|(\d+\.\d+)', tmp)
	print ('sadness')
