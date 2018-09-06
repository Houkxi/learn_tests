import argparse
import re
from my_pars_stuff import pars_class


parser = argparse.ArgumentParser(description='The latest parsing version for computor_v1')
parser.add_argument('str', type=str, help='Write down one and only one second degree equation string')
args = parser.parse_args()

parse = parse_class(str_check='\A[0-9^ \.\=\+\-\*/xX]\Z')
eqstr = pars_class().for_computor_v1(args.str)
print eqstr
