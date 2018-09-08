import re
import argparse
from instr_class import facts, instr_class

parser = argparse.ArgumentParser(description="send in a file with it's path")
parser.add_argument('str', type=str, help='file')
args = parser.parse_args()

file_obj = open(args.str, 'r')

###		Better readability		###
# text = file_obj.read()
# print text
# sentences = text.split('\n')

sentences = file_obj.read().split('\n')
new_file = []
i = 0
facts = facts()
facts.__init__(all_facts=facts.set_facts())
print facts.allf

for sent in sentences:
	tmp = sent.split('#')[0]
	if tmp:
		if tmp[0] == '=':
			facts.facts_init(tmp)
		else:
			new_file.append(tmp)


for obj in new_file:
	print obj

print facts.allf
