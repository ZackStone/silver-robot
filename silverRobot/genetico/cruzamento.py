import random
from .config import Config

class Cruzamento:
	def podeCruzar():
		r = random.uniform(0.0, 1.0)
		pode = (r <= Config.taxaCruzamento)
		return pode
		
	def cruzar(populacao):
		#print('\n\n')

		i0 = populacao[0]
		i1 = populacao[1]

		'''
		print(i0)
		print(i1)
		'''

		tamanho = len(i0.nums)
		metade = int(tamanho / 2)
		
		corte = random.randint(0, tamanho-1)
		metade = corte
		
		'''
		print(metade)
		'''

		i0a = i0.nums[0:metade]
		i0b = i0.nums[metade:tamanho]

		i1a = i1.nums[0:metade]
		i1b = i1.nums[metade:tamanho]

		i0.nums = i0a + i1b
		i1.nums = i1a + i0b

		'''
		print(i0)
		print(i1)
		'''

		populacao = [i0, i1]

		return populacao
