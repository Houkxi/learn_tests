import sys
import head

str = "I'm a string"
chari = 'test'
nb = 42
flt = 852.3219548544
i = 0
lst = []
animals = ['horse', 'cow', 'crow', 'dog']

def sestentua():
	hgt = 20
	lenght = 40
	print '-' * 65
	for i in range (1, lenght, (lenght / hgt)):
		print ' ' * ((lenght / 2) - (i / 2)), '*' * i, ' ' * ((lenght / 2) - i)

def moyenne():
	moy = 0
	notes = [15, 4, 19, 3, 7]
	print '-' * 65
	for i in notes:
		moy += i
	moy /= len(notes)
	print 'Moyenne : ', moy

def chge_ort():
	it = 0
	nbs = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
	print '-' * 65
	while it < len(nbs):
		if (nbs[it] % 2) != 0:
			nbs[it] += 1
		print nbs[it]
		it += 1

def matrice_test():
	line = [1, 2, 3]
	mat = [line, line, line]
	print 'line     col'
	# for a in len(mat):
	# 	for b in len(mat[a]):
	# 		print a, ' ' * 5, b

def fill_lst(lst):
	lst = lst + [15]
	lst = lst + [-22]
	print lst[0]
	print lst[1]
	lst.append(785)
	lst.append(7)
	print lst[2]
	print lst[3]

def ft_test(str, int):
	k = 0;
	i = len(str)
	k += nb * i
	print '-' * 65
	print '1 : {0} 2 : {1}' .format(str, nb, flt), ' 3 : {:.3f}' .format(flt)
	print k, i

def main():
	print '-' * 65
	print 'Hello pyton world'
	print sys.argv, chari
	print 'A' * int(sys.argv[1]), 'GC' * int(sys.argv[2])
	print '-' * 65
	for i in range(len(animals)):
		print animals[i]
	print '-' * 65
	print list(range(0, 99, 9))
	ft_test(str, nb)
	fill_lst(lst)
	sestentua()
	moyenne()
	chge_ort()
	matrice_test()

if __name__ == '__main__':
    main()
