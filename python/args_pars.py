import argparse


parser = argparse.ArgumentParser("Truely leatrn this shit")
parser.add_argument('--fo', action='store_true')
parser.add_argument('--str', type=str, action='store')
parser.add_argument('--end', action='store_true')
test = 'a'
args = parser.parse_args()
if args.fo is True:
	while True:
		test = input()
		args = parser.parse_args(test.split())
		if args.end is True:
			break
			# exit("Ended")
	print args
else:
	parser.add_argument('str', type=str)
	args = parser.parse_args()
