from .config import Config
from .individuo import Individuo
import random

class Populacao:
	def gerarPopulacaoInicial():
		populacao = []
		for i in range(0, Config.tamanhoPopulacao):
			nums = []
			for j in range(0, len(Config.numeros)):
				r = random.randint(0, Config.classes-1)
				nums.append(r)
			individuo = Individuo(nums)		
			populacao.append(individuo)
		return populacao
