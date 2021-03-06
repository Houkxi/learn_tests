import re
import argparse
# from my_math import is_all_float

def reshape_string(s, pattern=['[ \t]+'], sub=[' '], msg=None):
	i = 0
	print (len(pattern), len(sub))
	if len(pattern) != len(sub):
		print ('In reshape_string not the same amount between pattern and sub')
		exit()
	while i < len(pattern):
		tmp = re.sub(pattern[i], sub[i], s)
		if tmp is None:
			print ('REshape error')
			exit()
		s = tmp
		i += 1
	if msg != None:
		print ('No patterns found in string')
	return s

class ParsedStringClass():
	patterns = [
	'\A[()0-9^ \.\=\+\-\*/xX]+\Z',
	'\A(?<=[0-9^ \.\=\+\-\*/xX])+=(?=[0-9^ \.\=\+\-\*/xX])+\Z',
	''
	]
	base_reshape = ['[ \t]+', 'X', '(?<=[^x])x ?(?=[0-9]+)', 'x(?=[^\^])']
	base_sub = [' ', 'x', 'x^', 'x^1']
	def __init__(self, string):
		self.str = string

	def chars_cmp_str(self, s, cmp):
		tmp = re.search(cmp, s)
		if tmp == None:
			print ('Wrong character in equation, -h for more details')
			exit ()

	def nbrs_check(self, s):
		print (s)
		tmp = re.search('(\d+ +(?=[^\+\-\*\/])\d+)|(\d+ +(?=[^\+\-\*\/])[xX])', s)
		print (tmp)
		if tmp is not None:
			print('No operator between numbers')
			exit()

	def check_init_str(self):
		s = self.str
		self.chars_cmp_str(s, self.patterns[0])
		s = reshape_string(s, pattern=self.base_reshape, sub=self.base_sub)
		self.nbrs_check(s)
		print ('Checkeed string	< ' + s + ' >')
		return s

def parentheses_checker(s):
	count_left = 0
	parentheses_regex = re.search('(?<=\() *-?\d+\.*\d* *[\+\-\*] *-?\d+\.*\d*(?=\))', s)
	print ("Paren regex	", parentheses_regex)
	s = reshape_string(s, pattern=['[0-9^ \.\=\+\-\*/xX]+'], sub=[''])
	if s is not None:
		for paren in s:
			if paren == '(':
				count_left += 1
			elif paren == ')' and count_left > 0:
				count_left -= 1
			else:
				print ('Error in parentheses, check their positions')
				exit()
	print (count_left)
	if count_left != 0:
		print ('Error in parentheses, check their positions')
		exit()
	return True


class ParsOperandsClass(object):
	patterns = [
	' *\- ',
	'(?<=[xX0-9]) *= *(?=[xX0-9])',
	'(?<=[0-9()])\*',
	'\*(?=[0-9()xX])',
	'(?<=[0-9()])\+',
	'\+(?=[0-9()xX])',
	' *\* *(?=\()|(?<=\)) *\* *',
	]
	subs = [' + -', ' = ', ' *', '* ', ' +', '+ ', '']
	def __init__(self, string):
		self.str = string

	def reshape_operands(self):
		s = self.str
		s = parentheses_checker(s)
		s = reshape_string(s, pattern=self.patterns, sub=self.subs)
		print ('Operand string	< ' + s + ' >')
		return s

class numerical_pars():
	"""docstring for numerical_pars."""
	def __init__(self, tab_l, tab_r):
		self.tl = tab_l
		self.tr = tab_r

	def fraction_shit(self, s):
		#if re.search('((\d+\.\d+/\d+\.\d+)|(-\d+\.\d+/-\d+\.\d+))|((-\d+\.\d+/\d+\.\d+)|(\d+\.\d+/-\d+\.\d+)|(-\d+/-\d+)|(\d+/\d+)|(-\d+/\d+)|(\d+/-\d+))', s):
		# print ('Fraction shit :\n', s)
		if re.search('-*\d+\.*\d*/-*\d+\.*\d*', s):
			print ('Fraction shit :\n', s)
			a = re.search('\A-*\d+\.*\d*', s)
			b = re.search('(?<=/)-*\d+\.*\d*(?=\D)', s)
			a = float(a.group())
			b = float(b.group())
			print( '------> A', a, '<-> B', b, '<-> A/B', float(a / b))
			# print ('------>', a, b, float(a / b))
			tmp = str(a / b)
			s = re.sub('-*\d+\.*\d*/*-*\d+\.*\d*', tmp, s)
			print ('My floated version', s, '\n')
			# print ('My floated version', s)
			return s
		return s

	def already_simplfied(self, s):
		if re.search('(\d+\D\^\d+)|(-\d+\D\^\d+)', s) != None:
			if  re.search('(\d+\D\^0)|(-\d+\D\^0)', s) != None:
				s = re.sub('\D\^0', '', s)
			print ('Already simplified')
			# print ('Already simplified')
			return s

	def simplification(self, s):
		if self.already_simplfied(s) != None:
			s = self.already_simplfied(s)
			return s
		s = self.fraction_shit(s)
		if re.search('((\d+ *\** *-*\D\^?(?=\d*)))', s) != None:
			if  re.search('\D\^0', s) != None:
				s = re.sub(' *\** *\D\^0', '', s)
			else:
				s = re.sub(' *\** *', '', s)
			return s
		elif is_all_float(s) == True:
			return s
		elif re.match('(\+* *-*\D\^\d+)', s) != None:
			if s[-1] == '0':
				s = '1'
			return s
		else:
			print ('Error of some sort')
			exit()

	def simplify(self, tab):
			i = 0
			while i < len(tab):
				tab[i] = self.simplification(tab[i])
				i += 1
			return tab

	def started(self, tab_l, tab_r):
		tab_l = self.simplify(tab_l)
		tab_r = self.simplify(tab_r)
		return tab_l, tab_r
