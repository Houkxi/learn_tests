import argparse
import re
from my_pars_stuff import pars_class
from my_pars_stuff import numerical_pars
from one_sided import one_sided
import degree_solve

parser = argparse.ArgumentParser(description='Write a Second degree equation')
#parser.add_argument('-d', metavar='opt', type=str, help='Not the easiest function to use')
parser.add_argument('str', metavar='N', type=str, help='Not the easiest function to use')
args = parser.parse_args()

print '*' * 24, 'START', '*' * 24, '\n'
# print ('*' * 24, 'START', '*' * 24, '\n')
print '<', args.str, '>\n'
# print ('<', args.str, '>\n')

def equation_degree(tab, lvl=2, degree=0):
	print ('*' * 10, 'Equation Degree', '*' * 10)
	for elem in tab:
		if elem != None:
			if re.search('\D\^\d+\Z', elem):
				tmp = re.search('\d+\Z', elem)
				if int(tmp.group()) > lvl:
					print ('TOO HIGH of an equation degree:\n	- Current degree lvl =', tmp.group(), '\n	- Max degree lvl =', lvl)
					exit()
				elif int(tmp.group()) < 0:
					print ('TOO LOW of an equation degree:\n	- Current degree lvl =', tmp.group(), '\n	- Min degree lvl =', 0)
					exit()
				print (tmp.group())
				if degree < int(tmp.group()):
					degree = int(tmp.group())
	# print ('*' * 10, 'Ended of Degree', '*' * 10)
	return degree

def send_to_degree(eqt, degr, lvl):
	if lvl == 2:
		degree_solve.second_degree(eqt, degr)
	elif lvl == 1:
		degree_solve.first_degree(eqt, degr)
	elif lvl == 0:
		degree_solve.no_degree(degr[2])
	else:
		print ('Decide Later for bigger degrees')
		exit()

pars = pars_class(str_check='\A[0-9^ \.\=\+\-\*/xX]+\Z', pattern_tab=['[ \t]+', ' *\- ', ' *\+ *'], change_tab=[' + -', 'a'], split_tab=[' = ', 'a'])
pars.__init__(str_check='\A[0-9^ \.\=\+\-\*/xX]+\Z', pattern_tab=['[ \t]+', ' *\- ', ' *\+ *'], change_tab=[' + -', 'a'], split_tab=[' = ', 'a'])
tab_l, tab_r = pars.for_computor_v1(args.str)
print 'TABs :\n', tab_l, '\n', '***' * 15, '\n', tab_r, '\n'
# print (tab_l, '\n', '***' * 15, '\n', tab_r)
num_pars = numerical_pars(tab_l, tab_r)
num_pars.started(tab_l, tab_r)
print 'TABs :\n', tab_l, '\n', '***' * 15, '\n', tab_r, '\n'
# print (tab_l, '\n', '***' * 15, '\n', tab_r)
side_pars = one_sided(['\D\^1', '\D\^2'], ['x^1', 'x^2'])
eqt, degre = side_pars.lets_go(tab_l, tab_r)
dgr = equation_degree(eqt)
print 'Degree = ', dgr, 'ABCs :', degre, 'Eqt :', eqt
print '*' * 10, 'Ended of Degree', '*' * 10, '\n'
# print ('Degree = ', dgr, 'ABCs :', degre, 'Eqt :', eqt)
send_to_degree(eqt, degre, dgr)
