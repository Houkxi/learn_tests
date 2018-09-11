import re
import argparse
from instr_class import facts, instr_class

parser = argparse.ArgumentParser(description="send in a file with it's path")
parser.add_argument('str', type=str, help='file')
args = parser.parse_args()

file_obj = open(args.str, 'r')
sentences = file_obj.read().split('\n')
new_file = []
facts = facts()
facts.__init__(all_facts=facts.set_facts())
print (facts.allf, "\n")

for sent in sentences:
	tmp = sent.split('#')[0]
	if tmp:
		if tmp[0] == '=':
			facts.facts_init(tmp)
		else:
			new_file.append(tmp)

for obj in new_file:
	print (obj)

print ("\n", facts.allf)

def check_true(facts, list_cmd=0, goal=0):
	check_goal(checks initial facts with goal, then checks list_cmd to find the instruction returns new goal)
	if list_cmd == True:
		return something and go back to what wasn't true'

#try recursive python for the algorithm
#A dictionary with the implications as keys
