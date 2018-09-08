import re

class facts():
	"""docstring for facts."""
	def __init__(self, all_facts={}):
		self.allf = all_facts

	def set_facts(self):
		facts = {}
		for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			print letter
			facts[letter] = False
		return facts

	def facts_init(self, str):
		if re.search("=", str):
			str = str.split('=')[1]
		for letter in str:
			if self.allf.get(letter) == False:
				self.allf[letter] = True
		# return self.allf


class instr_class():
	"""docstring for instr_class."""
	def __init__(self):
		pass

	def priority_check(self, pattern=['\A *(\!*[A-Z] *[|\+\^] *\!*[A-Z])']):
		pass

	def line_pars(self, str):
		hashed = priority_check(str)
		return object
