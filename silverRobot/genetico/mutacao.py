import random
from .config import Config

class Mutacao:
	def podeMutar():
		r = random.uniform(0.0, 1.0)
		pode = (r <= Config.taxaMutacao)
		return pode

	def mutar(populacao):
		for individuo in populacao:
			
			# muda todos os genes do individuo
			''' 			
			for n in range(0, len(individuo.nums)):
				individuo.nums[n] = random.randint(0, Config.classes-1)
			'''

			# muda apenas um gene do individuo
			r = random.randint(0, len(individuo.nums)-1)
			individuo.nums[r] = random.randint(0, Config.classes-1)
			
		return populacao