import os
import numpy as np   
import sys
from decimal import Decimal
import time

from lib.gerarTxt import gerarTxt
from lib.silverRobot import run, printGlobals, printDiffMax

# ============================================

fileName = 'input.txt'
nums = []
classes = 0

# ============================================

def gerarArquivo():
	# 			numType, 	high, 	size, 	fileName, 	numClasses):
	gerarTxt(	'i', 		10000, 	10000, 	fileName, 	100)

def lerArquivo():
	global nums, classes

	curpath = os.path.dirname(os.path.abspath(__file__))
	filepath = os.path.join(curpath, 'temp', fileName)

	f = open(filepath, 'r')
	classes = int(f.readline())
	nums = []
	for line in f:
		a = line.split(';')
		for n in a:
			nums.append(Decimal(n))

def main():
	start_time = time.time()
	run(nums, classes)
	print(str(round(time.time() - start_time, 3)) + " seconds")
	printDiffMax()
	#printGlobals()

# ============================================
# ============================================

if len(sys.argv) > 1:
	fileName = sys.argv[1]
else:
	print('Gerando Arquivo')
	gerarArquivo()
	print('Arquivo Gerado')

print('Lendo Arquivo')
lerArquivo()
print('Arquivo Lido')
print('Iniciando separacao')
main()
print('Fim')