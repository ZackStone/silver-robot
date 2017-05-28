class Fitness:
	def calcularFitness(populacao):
		for i in range(0, len(populacao)):
			populacao[i].calcularFitness()
		return populacao