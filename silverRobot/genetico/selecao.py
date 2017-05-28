from .config import Config
import random

class Selecao:
	def torneio(populacao, qtd):
		selecionados = []		
		for i in range(0, qtd):
			r = random.randint(0, len(populacao)-1)
			individuo = populacao[r]
			selecionados.append(individuo)
		return selecionados

	def torneioBinario(populacao):
		return Selecao.torneio(populacao, 2)

	def melhores(populacao):
		pop = sorted(populacao, key=lambda x: x.fitness)
		pop = pop[0:Config.qtdIndividuosElitismo]
		return pop

	def melhor(populacao):
		pop = sorted(populacao, key=lambda x: x.fitness)
		return pop[0]