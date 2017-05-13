from random import randint
import numpy as np   
import sys
from decimal import Decimal

def randomInt(high, size):
	a = np.random.randint(high, size=(size, size))
	b = np.array2string(a[0], separator=';')
	b = b[1:len(b)-1]
	return b

def randomDecimal(high, size):
	a = np.random.uniform(low=0, high=high, size=(size,))
	b = np.array2string(a, separator=';')
	b = b[1:len(b)-1]
	return b

def writeFile(txt, fileName):
	txt = txt.replace('\n','')
	f = open('temp/'+fileName, 'w')
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

	txt = numClasses + '\r\n'

	if numType == 'd':
		txt += randomDecimal(Decimal(high), size)
	else:
		txt += randomInt(int(high), size)

	writeFile(txt, fileName)

try:
	clInput()
except:
	consoleInput()		