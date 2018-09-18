import argparse
import re
from my_pars_stuff import ParsedStringClass, ParsOperandsClass


parser = argparse.ArgumentParser(description='The latest parsing version for computor_v1')
parser.add_argument('str', type=str, help='Write down one and only one second degree equation string')
args = parser.parse_args()

### Paranthese priority and well formated check ###

parsed = ParsedStringClass(args.str).check_init_str()
parsed = ParsOperandsClass(parsed).reshape_operands()

print (len([' *\- ']), len([' + -']))
# parse = pars_class(str_check=['\A[()0-9^ \.\=\+\-\*/xX]+\Z', '\A(?<=[0-9^ \.\=\+\-\*/xX])+=(?=[0-9^ \.\=\+\-\*/xX])+\Z'])
# # Basic checks and reshapes, take out the whitespaces/ make sure there are operators
# eqstr = parse.check_init_str(args.str, pattern=['[ \t]+'], sub=[' '])
# # operator repositionning
# print ('Numbers of patterns ', len([' *\- ', '(?<=[xX0-9]) *= *(?=[xX0-9])', '(?<=[0-9()])\*', ' *\* *(?=\()|(?<=\)) *\* *']), len([' + -', ' = ', ' *', '']))
# # eqstr = parse.reshape_string(eqstr, pattern=[' *\- ', '(?<=[xX0-9]) *= *(?=[xX0-9])', '(?<=[0-9()])\*', ' *\* *(?=\()|(?<=\)) *\* *'], sub=[' + -', ' = ', ' *', ''])
# eqstr = parse.reshape_string(eqstr, pattern=[' *\- '], sub=[' + -'])
# print ('Minus operand parsed		< ' + eqstr + ' >')
# eqstr = parse.reshape_string(eqstr, pattern=['(?<=[xX0-9]) *= *(?=[xX0-9])'], sub=[' = '])
# print ('Equal sign parsed		< ' + eqstr + ' >')
# eqstr = parse.reshape_string(eqstr, pattern=['(?<=[0-9()])\*', '\*(?=[0-9()xX])'], sub=[' *', '* '])
# print ('Multiplication parsed		< ' + eqstr + ' >')
# eqstr = parse.reshape_string(eqstr, pattern=['(?<=[0-9()])\+', '\+(?=[0-9()xX])'], sub=[' +', '+ '])
# print ('Addition operand parsed		< ' + eqstr + ' >')
# eqstr = parse.reshape_string(eqstr, pattern=['(?<=[0-9()])\-'], sub=[' -'])
# print ('Minus operand parsed		< ' + eqstr + ' >')
# eqstr = parse.reshape_string(eqstr, pattern=[' *\* *(?=\()|(?<=\)) *\* *'], sub=[''])
# print ('Taking out operands		< ' + eqstr + ' >')
