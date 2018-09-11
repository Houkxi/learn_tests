import argparse
import re
from my_pars_stuff import pars_class


parser = argparse.ArgumentParser(description='The latest parsing version for computor_v1')
parser.add_argument('str', type=str, help='Write down one and only one second degree equation string')
args = parser.parse_args()

### Paranthese priority and well formated check ###

parse = pars_class(str_check=['\A[()0-9^ \.\=\+\-\*/xX]+\Z', '\A(?<=[0-9^ \.\=\+\-\*/xX])+=(?=[0-9^ \.\=\+\-\*/xX])+\Z'], pattern_tab=['[ \t]+'], change_tab=[' + -'])
# Basic checks and reshapes, take out the whitespaces/ make sure there are operators
eqstr = parse.check_init_str(args.str)
# operator repositionning
eqstr = parse.reshape_string(eqstr, pattern=' *\- ', sub=' + -')
eqstr = parse.reshape_string(eqstr, pattern='(?<=[xX0-9]) *= *(?=[xX0-9])', sub=' = ')
eqstr = parse.reshape_string(eqstr, pattern='(?<=[0-9()])\*', sub=' *')
eqstr = parse.reshape_string(eqstr, pattern=' *\* *(?=\()|(?<=\)) *\* *', sub='')
print 'Parsed string	< ' + eqstr + ' >'
