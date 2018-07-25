from my_pars_stuff import is_all_float
import re

class one_sided():
	"""docstring for one_sided."""
	def __init__(self, pattern_tab=None, ret=None):
		self.patts = pattern_tab
		self.ret = ret

	def add_up_c(self, tab, ctmp=0):
		for elem in tab:
			if is_all_float(elem) == True:
				ctmp += float(elem)
		print (ctmp)
		if re.search('\.0\Z', str(ctmp)) != None:
			ctmp = int(ctmp)
			print (ctmp)
		return ctmp

	def add_up_xs(self, tab, pattern=None, ret=None, atmp=0):
		for elem in tab:
			if re.search(pattern, elem) != None:
				if re.search('(-\D\^\d+)', elem):
					tmp = re.search('-1', '-1')
				elif re.search('(\A\D\^\d+)', elem):
					tmp = re.search('1', '1')
				else:
					tmp = re.search('(-*\d+\.*\d*)', elem)
					print (tmp.group())
					print ('---->', tmp.group())
				atmp += float(tmp.group())
				print (atmp)
		atmp = round(atmp, 10)
		print ('Ax = ', atmp)
		if re.search('\.0\Z', str(atmp)) != None:
			atmp = int(atmp)
			print (atmp)
		if atmp == 0:
			return None, 0
		if atmp == -1:
			return '-' + ret, atmp
		if atmp == 1:
			return ret, atmp
		return str(atmp) + ret, atmp

	def side_prep(self, tab):
		i = 0
		while i < len(tab):
			if tab[i][0] == '-':
				tab[i] = re.sub('-', '', tab[i])
			else:
				tab[i] = '-' + tab[i]
			i += 1
		return tab

	def lets_go(self, tab_l, tab_r):
		tab_r = self.side_prep(tab_r)
		tab_l = tab_l + tab_r
		c = self.add_up_c(tab_l)
		bx, b = self.add_up_xs(tab_l, '\D\^1', ret='x^1')
		ax, a = self.add_up_xs(tab_l, '\D\^2', ret='x^2')
		print ('+-'* 25, '+')
		print (ax, '+', bx, '+', c, '= 0')
		print ('+-'* 25, '+')
		eqt = [ax, bx, str(c)]
		degr = [float(a), float(b) , float(c)]
		return eqt, degr
