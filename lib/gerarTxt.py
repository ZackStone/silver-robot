from random import randint
import numpy as np
import sys
from decimal import Decimal
import os

def randomInt(high, size):
	a = np.random.randint(high, size=(size,))
	b = ';'.join(map(str, a))
	return b

def randomDecimal(high, size):
	a = np.random.uniform(low=0, high=high, size=(size,))
	b = ';'.join(map(str, a))
	return b

def writeFile(txt, fileName):
	txt = txt.replace('\n','')

	curpath = os.path.dirname(os.path.abspath(__file__))
	temppath = os.path.join(curpath, '..', 'temp')

	if not os.path.exists(temppath):
		os.makedirs(temppath)

	filepath = os.path.join(temppath, fileName)
		
	f = open(filepath, 'w')
	f.write(txt)
	f.close()

def consoleInput():
	numType = ''
	high = None
	size = None
	fileName = ''
	txt = ''

	while numType not in  ['i', 'd']:
		numType = input('[i]nt or [d]ouble? ')

	size = int(input('size: '))

	if numType == 'd':
		high = int(input('high: '))
		txt = randomDouble(high, size)		
	else:
		high = Decimal(input('high: '))
		txt = randomInt(high, size)

	fileName = input('File name: ')

	writeFile(txt, fileName)

def clInput():
	numType = sys.argv[1]
	high = sys.argv[2]
	size = int(sys.argv[3])
	fileName = sys.argv[4]
	numClasses = sys.argv[5]


def gerarTxt(numType, high, size, fileName, numClasses):
	txt = str(numClasses) + '\r\n'

	if numType == 'd':
		txt += randomDecimal(Decimal(high), size)
	else:
		txt += randomInt(int(high), size)

	writeFile(txt, fileName)

def main():
	try:
		clInput()
	except:
		consoleInput()

# ============================================
# ============================================

if 'gerar_txt.py' in sys.argv[0]:
	main()