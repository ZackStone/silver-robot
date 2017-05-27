import os
import sys
from decimal import Decimal
import operator
import numpy as np
import time
import datetime

# ============================================

mat = []
matsum = dict()
matix = []

# ============================================

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

	ix = updateIndex()
	mat[ix].append(num)
	matsum[ix] += num

def updateIndex():
	global mat, matsum, matix

	matix = sorted(matsum.items(), key=operator.itemgetter(1))
	if len(matix) <= 0: 
		return 0
	return matix[0][0]

def diffMax():
	dmax = matix[len(matix)-1][1]
	dmin = matix[0][1]
	diff = str(dmax - dmin)
	return diff


def grupos():
	out = ''
	for i in mat:
		linha = (str(sum(i)) + ';' +  ';'.join(map(str, i)))
		out += (linha + '\n')
	return out	

def guloso_run(nums, classes):
	initialize()
	nums.sort(reverse=True)
	for i in range(0, len(nums)):
		ix = i % classes
		insertNum = nums[i]
		insert(insertNum, ix)

	diffMaxstr = 'Diferenca maxima entre os grupos: ' + diffMax()
	output_str = grupos().replace('\n', '<br>') 
	retorno = output_str + '<br>' + diffMaxstr

	return retorno