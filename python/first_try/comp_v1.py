import argparse
import sys
import re

tab = []
ct = 0

parser = argparse.ArgumentParser(description='Is this working to start my parsing')
# parser.add_argument('Str', metavar='Str', type=str, help='Write the correct form of string')
parser.add_argument('Str', metavar='Str', type=str, help='Write the correct form of string')
# help(parser.add_argument)
# parser.add_argument('*', dest='accumulate', action='store_const', const=sum, help='Test for *')
# parser.add_argument('X^', metavar='Str', type=str, help='Lets see')

args = parser.parse_args()

print args.Str

# a,b,c = re.split('\X^+', args.Str, 1)

# print a, b, c

tab = args.Str.split(" ")

while ct < len(tab):
	print tab[ct]
	ct += 1

a = re.search(r'(\d\.\d) \* (\D+)(\d+)', args.Str)
# b = re.search(r'(\d*) \* (\D+)(\d+)', args.Str)
# a = re.search(r'[(\d\.\d) (?:(\d*))] \* (\D+)(\d+)', args.Str)
re.split(r'(\d+) \* (\D+)(\d+)', args.Str)
print args.Str
print a.group(0)

b = re.search(r'(\d*) \* (\D+)(\d+)', args.Str)

print b.group(0)

# def check_eq_degree(tab):
# 	i = 0
# 	ct = 0
# 	while tab[ct]:
# 		if re.
