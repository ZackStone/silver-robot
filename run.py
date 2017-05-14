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
	gerarTxt('i', 100, 900, fileName, 10)

def lerArquivo():
	global nums, classes

	f = open('temp/' + fileName, 'r')
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

print('Gerando Arquivo')
gerarArquivo()
print('Arquivo Gerado')
print('Lendo Arquivo')
lerArquivo()
print('Arquivo Lido')
print('Iniciando separacao')
main()
print('Fim')