from config import Config

class Individuo:
	nums = []
	fitness = None
	def __init__(self, nums):
		self.nums = nums
	def __str__(self):
		return 'fitness: ' + str(self.fitness) + ' | nums: ' + str(self.nums)
	
	def calcularFitness(self):
		soma = [0] * Config.classes
		for i in range(0, len(self.nums)-1):
			classe = self.nums[i]
			soma[classe] += Config.numeros[i]
		fitness = max(soma) - min(soma)
		self.fitness = fitness

		
		print(self)
		print(soma)
		print('.')