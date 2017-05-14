import os
import numpy as np   
import sys
from decimal import Decimal

from lib.gerarTxt import gerarTxt
from lib.silverRobot import run


fileName = 'teste.txt'
gerarTxt('i', 50000, 1000, fileName, 20)

f = open('temp/' + fileName, 'r')
classes = int(f.readline())
nums = []
for line in f:
	a = line.split(';')
	for n in a:
		nums.append(Decimal(n))

run(nums, classes)