import os
import numpy as np   
import sys
from decimal import Decimal

_nums = None

def run(nums, classes):
	nums.sort()
	print('Numero de classes: ' + str(classes))
	print(nums)


