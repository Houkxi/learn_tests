import argparse
import re
from side_fcts import is_all_float
import degree_solve

parser = argparse.ArgumentParser(description='Write a Second degree equation')
#parser.add_argument('-d', metavar='opt', type=str, help='Not the easiest function to use')
parser.add_argument('str', metavar='N', type=str, help='Not the easiest function to use')
args = parser.parse_args()

print (args.str)

def debug_visu(tab1=None, tab2=None):
	print '*' * 20
	if tab1 !=  None:
		i = 0
		while i < len(tab1):
			print '+> ', tab1[i]
			i += 1
	if tab2 !=  None:
		i = 0
		while i < len(tab2):
			print '-> ', tab2[i]
			i += 1
	print '*' * 20

def check_str(pattern, s):
	a = re.search(pattern, s)
	if a == None:
		print ('Wrong character in equation')
		exit ()

def side_prep(tab):
	i = 0
	while i < len(tab):
		if tab[i][0] == '-':
			tab[i] = re.sub('-', '', tab[i])
		else:
			tab[i] = '-' + tab[i]
		i += 1
	return tab

def already_simplfied(s):
	if re.search('(\d+\D\^\d+)|(-\d+\D\^\d+)', s) != None:
		if  re.search('(\d+\D\^0)|(-\d+\D\^0)', s) != None:
			s = re.sub('\D\^0', '', s)
		print ('Already simplified')
		return s

def simplification(s):
	if already_simplfied(s) != None:
		s = already_simplfied(s)
		return s
	if re.search('(( \* \D\^\d+)|( \* \D\^\d+))', s) != None:
		if  re.search('\D\^0', s) != None:
			s = re.sub(' \* \D\^0', '', s)
		else:
			s = re.sub(' \* ', '', s)
		return s
	elif is_all_float(s) == True:
		return s
	elif re.match('(\D\^\d+)|(-\D\^\d+)', s) != None:
		if s[-1] == '0':
			s = '1'
		return s
	else:
		print ('Error of some sort')
		exit()

def add_up_c(tab, ctmp=0):
	for elem in tab:
		if is_all_float(elem) == True:
			ctmp += float(elem)
	print ctmp
	if re.search('\.0\Z', str(ctmp)) != None:
		ctmp = int(ctmp)
		print ctmp
	return ctmp

def add_up_xs(tab, pattern, ret=None, atmp=0):
	for elem in tab:
		if re.search(pattern, elem) != None:
			if re.search('(-\D\^\d+)', elem):
				tmp = re.search('-1', '-1')
			elif re.search('(\A\D\^\d+)', elem):
				tmp = re.search('1', '1')
			else:
				tmp = re.search('((-\d+\.\d+)|(\d+\.\d+)|(-\d+)|(\d+))', elem)
			atmp += float(tmp.group(0))
	atmp = round(atmp, 10)
	print 'Ax = ', atmp
	if re.search('\.0\Z', str(atmp)) != None:
		atmp = int(atmp)
		print atmp
	if atmp == 0:
		return None, 0
	if atmp == -1:
		return '-' + ret, atmp
	if atmp == 1:
		return ret, atmp
	return str(atmp) + ret, atmp

def equation_degree(tab, lvl=2, degree=0):
	print '*' * 10, 'Equation Degree', '*' * 10
	for elem in tab:
		if re.search('\D\^\d+\Z', elem):
			tmp = re.search('\d+\Z', elem)
			if int(tmp.group()) > lvl:
				print 'TOO HIGH of an equation degree:\n	- Current degree lvl =', tmp.group(), '\n	- Max degree lvl =', lvl
				exit()
			elif int(tmp.group()) < 0:
				print 'TOO LOW of an equation degree:\n	- Current degree lvl =', tmp.group(), '\n	- Min degree lvl =', 0
				exit()
			print tmp.group()
			if degree < int(tmp.group()):
				degree = int(tmp.group())
	print '*' * 10, 'Ended of Degree', '*' * 10
	return degree

def send_to_degree(eqt, degr, lvl):
	print 'Degree' , lvl
	if lvl == 2:
		degree_solve.second_degree(eqt, degr)
	elif lvl == 1:
		degree_solve.first_degree(eqt, degr)
	elif lvl == 0:
		degree_solve.no_degree(degr[2])
	else:
		print 'Decide Later for bigger degrees'
		exit()

def visu_color_test(arg):
	pass

check_str('\A[0-9^ \.\=\+\-\*/xX]+\Z', args.str)
left = re.sub(' - ', ' + -', args.str)
left = re.sub('( \+ )', 'a', left)
print 'Post sub + - : ', left
right = left.split(' = ')
left = right[0]
right = right[1]
print 'Post sub : \n', left, '\n', right
tab_l = left.split('a')
tab_r = right.split('a')

if tab_r == None:
	tba_r = right

i = 0
while i < len(tab_l):
	tab_l[i] = simplification(tab_l[i])
	i += 1

i = 0
while i < len(tab_r):
	tab_r[i] = simplification(tab_r[i])
	i += 1
debug_visu(tab_l, tab_r)
tab_r = side_prep(tab_r)
debug_visu(tab_l, tab_r)
tab_l = tab_l + tab_r
debug_visu(tab_l)

dgr = equation_degree(tab_l)
print 'My Degree = ', dgr
c = add_up_c(tab_l)
bx, b = add_up_xs(tab_l, '\D\^1', ret='x^1')
ax, a = add_up_xs(tab_l, '\D\^2', ret='x^2')
print ax, '+', bx, '+', c, '= 0'

eqt = [ax, bx, str(c)]
degr = [a, b , c]
dgr = equation_degree(eqt)
print 'My Degree = ', dgr
send_to_degree(eqt, degr, dgr)

delta = (b * b) -4 * (a * c)
print delta
