import re

def is_all_float(arg):
	try:
		float(arg)
		return True
	except ValueError:
		return False

def is_all_int(arg):
	print (str(arg))
	tmp = re.search('\.(?=[1-9]*)', str(arg))
	print (tmp)
	if  tmp != None:
		return False
	return True

def count_every_ten(nb, direction=0, show=0):
	ct = 0
	div = 10
	print(is_all_int(nb), int(nb), nb)
	if direction >= 0:
		while nb > 10:
			nb = nb / div
			ct += 1
			if show != 0:
				print (nb, '/', div)
	elif direction < 0:
		while is_all_int(nb) == False:
			nb = nb * div
			ct += 1
			if show != 0:
				print (nb, '*', div)
	print ('Counter =', ct)

def group_in_twos_m(s, length):
	x = -1
	tmp1 = []
	tmp2 = ''
	print s
	while x >= -length:
		if (x - 1 >= -length):
			tmp2 = s[x - 1]
		tmp2 += s[x]
	 	tmp1 += [tmp2]
		tmp2 = ''
		x -= 2
	x = -1
	tmp2 = []
	while x >= -len(tmp1):
		tmp2 += [tmp1[x]]
		x -= 1
	return tmp2

def group_in_twos_p(s, length):
	x = 0
	tmp1 = []
	tmp2 = ''
	print s
	while (x + 1) <= length:
		tmp2 = s[x]
		if ((x + 1) < length):
			tmp2 += s[x + 1]
		if (x + 1 >= length):
			tmp2 += '0'
	 	tmp1 += [tmp2]
		tmp2 = ''
		x += 2
	return tmp1

def pars_number_in_pairs(nb):
	print ('The number =', nb, 'str : ' + str(nb), is_all_float(nb))
	tmp = str(nb).split('.')
	print tmp
	left = group_in_twos_m(tmp[0], len(tmp[0]))
	right = group_in_twos_p(tmp[1], len(tmp[1]))
	left += ['.']
	left += right
	print (left)
	return left

def to_decimal(nb):
	while nb > 1:
		nb /= 10
	return nb

def square_root(nb_grp):
	i = 0
	n = 0
	m = 0
	tmp = 0
	res = 0
	div = 1
	while n * n <= float(nb_grp[0]):
		n += 1
	n -= 1
	print n
	res = float(n)
	n = n * 2
	while nb_grp[i] != '.':
		if i == 0:
			tmp = float(nb_grp[0]) - n
		print tmp, nb_grp[0]
		if nb_grp[i + 1] == '.':
			break;
		i += 1
		tmp = (tmp * 100) + float(nb_grp[i])
		print tmp
		while ((n * 10) + m) * m <= tmp:
			print '((', n, '* 10) + ', m, ') * ', m
			m += 1
		m -= 1
		print tmp, ' - ((', n, '* 10) + ', m, ') * ', m, ' = ', tmp - ((n * 10) + m) * m
		tmp -= ((n * 10) + m) * m
		res = (res * 10) + m
		n = res * 2
		m = 0
		print 'RES', res, ',', n
	i += 2
	while i < len(nb_grp):
		tmp = (tmp * 100) + float(nb_grp[i])
		n = res * 2
		while ((n * 10) + m) * m <= tmp:
			print '((', n, '* 10) + ', m, ') * ', m
			m += 1
		m -= 1
		tmp -= ((n * 10) + m) * m
		res = (res * 10) + m
		div *= 10
		n = res * 2
		m = 0
		i += 1
		print 'RES', res / div, ',', n
	return res / div
