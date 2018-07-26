import argparse
import Tkinter
import sys


fenetre = Tkinter.Tk()

widget = Tkinter.Button(None)
widget.config(text='Lets work', command=sys.exit)
widget.pack(expand=Tkinter.YES, fill=Tkinter.X)
# widget.pack()
widget.mainloop()
# label = Tkinter.Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()
# parser = argparse.ArgumentParser("Truely leatrn this shit")
# parser.add_argument('--fo', action='store_true')
# parser.add_argument('--str', type=str, action='store')
# parser.add_argument('--end', action='store_true')
# test = 'a'
# args = parser.parse_args()
# if args.fo is True:
# 	while True:
# 		test = input()
# 		args = parser.parse_args(test.split())
# 		if args.end is True:
# 			break
# 			# exit("Ended")
# 	print args
# else:
# 	parser.add_argument('str', type=str)
# 	args = parser.parse_args()
