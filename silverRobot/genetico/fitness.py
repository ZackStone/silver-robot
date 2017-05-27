class Fitness:
	def calcularFitness(populacao):
		for individuo in populacao:
			individuo.calcularFitness()
		return populacao