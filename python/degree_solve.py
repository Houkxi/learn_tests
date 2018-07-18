import re

def second_degree(eqt, degr):
	a = degr[0]
	b = degr[1]
	c = degr[2]
	print 'Second degree fct'
	delta = (b * b) -4 * (a * c)
	print delta

def first_degree(eqt, degr):
	b = degr[1]
	c = degr[2]
	print 'first degree fct'
	tmp = -c / b
	print 'x =', tmp

def no_degree(c):
	print 'No degree fct'
