import argparse
import sys

tab = []
ct = 0

parser = argparse.ArgumentParser(description='Is this working to start my parsing')
parser.add_argument('Str', metavar='Str', type=str, help='Write some form of string')
# help(parser.add_argument)
parser.add_argument('*', dest='accumulate', action='store_const', const=sum, help='Test for *')
parser.add_argument('X^', metavar='Str', type=str, help='Lets see')

args = parser.parse_args()

print args.Str

tab = args.Str.split(" ")

while ct < len(tab):
	print tab[ct]
	ct += 1
