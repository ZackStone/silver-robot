import os
import sys
from decimal import Decimal
import operator


mat = []
matsum = dict()
matix = []

def initialize():
	global mat, matsum, matix
	mat = []
	matsum = dict()
	matix = []

def insert(num, ix):
	global mat, matsum, matix

	if len(mat) <= ix:
		mat.append([])
	if ix not in matsum:
		matsum[ix] = 0

	print('ix: ' + str(updateIndex()))
	ix = updateIndex()
	mat[ix].append(num)
	matsum[ix] += num

def updateIndex():
	global mat, matsum, matix

	matix = sorted(matsum.items(), key=operator.itemgetter(1))
	if len(matix) <= 0: 
		return 0
	return matix[0][0]

def printGlobals():
	global mat, matsum, matix
	print('========================================')
	print()
	print('mat')
	print(mat)
	print()
	print()
	print('matsum')
	print(matsum)
	print()
	print()
	print('matix')
	print(matix)
	print()
	print('========================================')

def run(nums, classes):
	global mat, matsum, matix	

	initialize()
	nums.sort(reverse=True)
	print('Numero de classes: ' + str(classes))

	for i in range(0, len(nums)):
		ix = i % classes
		insert(nums[i], ix)

	printGlobals()




