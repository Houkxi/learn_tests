import re
import argparse
from my_math import is_all_float

class pars_class():
	"""docstring for pars_class."""
	def __init__(self, str_check=None, pattern_tab=None, change_tab=None, split_tab=None):
		self.strch = str_check
		self.patts = pattern_tab
		self.subs = change_tab
		self.splits = split_tab

	def reshape_string(self, s, pattern=' +', sub=' ', msg=None):
		tmp = re.sub(pattern, sub, s)
		if tmp:
			return tmp
		if msg != None:
			print ('No patterns found in string')
		return s

	def chars_cmp_str(self, s, cmp):
		tmp = re.search(cmp, s)
		if tmp == None:
			print (s, cmp)
			print ('Wrong character in equation, -help for more details')
			exit ()

	def for_computor_v1(self, s):
		s = self.reshape_string(s, self.patts[0])
		#s = self.reshape_string(s, '(?<=\ *-*)([xX])(?=\ \+*-*\Z?)', 'x^1', 'go')
		self.chars_cmp_str(s, self.strch)
		s = self.reshape_string(s, self.patts[1], self.subs[0])
		s = self.reshape_string(s, self.patts[2], self.subs[1])
		tab_l = s.split(self.splits[0])
		tab_r = tab_l[1]
		tab_l = tab_l[0].split(self.splits[1])
		tab_r = tab_r.split(self.splits[1])
		return tab_l, tab_r

class numerical_pars():
	"""docstring for numerical_pars."""
	def __init__(self, tab_l, tab_r):
		self.tl = tab_l
		self.tr = tab_r

	def fraction_shit(self, s):
		#if re.search('((\d+\.\d+/\d+\.\d+)|(-\d+\.\d+/-\d+\.\d+))|((-\d+\.\d+/\d+\.\d+)|(\d+\.\d+/-\d+\.\d+)|(-\d+/-\d+)|(\d+/\d+)|(-\d+/\d+)|(\d+/-\d+))', s):
		# print ('Fraction shit :\n', s)
		if re.search('-*\d+\.*\d*/-*\d+\.*\d*', s):
			print 'Fraction shit :\n', s
			a = re.search('\A-*\d+\.*\d*', s)
			b = re.search('(?<=/)-*\d+\.*\d*(?=\D)', s)
			a = float(a.group())
			b = float(b.group())
			print '------> A', a, '<-> B', b, '<-> A/B', float(a / b)
			# print ('------>', a, b, float(a / b))
			tmp = str(a / b)
			s = re.sub('-*\d+\.*\d*/*-*\d+\.*\d*', tmp, s)
			print 'My floated version', s, '\n'
			# print ('My floated version', s)
			return s
		return s

	def already_simplfied(self, s):
		if re.search('(\d+\D\^\d+)|(-\d+\D\^\d+)', s) != None:
			if  re.search('(\d+\D\^0)|(-\d+\D\^0)', s) != None:
				s = re.sub('\D\^0', '', s)
			print 'Already simplified'
			# print ('Already simplified')
			return s

	def simplification(self, s):
		if self.already_simplfied(s) != None:
			s = self.already_simplfied(s)
			return s
		s = self.fraction_shit(s)
		if re.search('((\d+ *\** *-*\D\^\d+))', s) != None:
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
