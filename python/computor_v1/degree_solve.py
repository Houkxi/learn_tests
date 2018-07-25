import re
import my_math


def one_value(a, b):
	res = -(b / (2 * a))
	print (res)
	return res

def two_positives(delta, a, b):
	print a, b, delta
	# my_math.count_every_ten(delta, direction=11, show=1)
	# tmp = my_math.find_perfect_sqr(delta)
	# delta -= tmp * tmp
	tmp = my_math.pars_number_in_pairs(delta)
	nb = my_math.square_root(tmp)
	b = b * -1
	x1 = (b - nb) / a
	x2 = (b + nb) / a
	print 'X1 =', x1, 'X2 =', x2

def two_complexes(delta, a, b):
	pass

def second_degree(eqt, degr):
	a = degr[0]
	b = degr[1]
	c = degr[2]
	delta = (b * b) -4 * (a * c)
	print 'Delta = ', delta
	if delta > 0:
		two_positives(delta, a, b)
	elif delta == 0:
		one_value(a, b)
	else:
		two_complexes(delta, a, b)

def first_degree(eqt, degr):
	b = degr[1]
	c = degr[2]
	print ('first degree fct')
	tmp = -c / b
	print ('x =', tmp)

def no_degree(c):
	print ('No degree fct')
