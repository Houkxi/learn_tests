import re
import argparse

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

for sent in sentences:
	new_file.append(sent.split('#')[0])

for obj in new_file:
	print obj
