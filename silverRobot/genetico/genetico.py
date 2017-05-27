from config import Config
from individuo import Individuo
from populacao import Populacao
from cruzamento import Cruzamento
from mutacao import Mutacao
from selecao import Selecao
from fitness import Fitness

class Genetico:

	individuos = []

	def __init__(self, individuos=[]):
		self.individuos = individuos

	def ag(self):
		print('####\n\t\tpopulacao inicial\n####')
		populacao = Populacao.gerarPopulacaoInicial()
		populacao = Fitness.calcularFitness(populacao)

		novaPopulacao = []
		# ate que o numero de geracoes finalize
		for i in range(0, Config.geracoes):
			print('####\n\t\tgeracao ' + str(i) + '\n####')
			
			while len(novaPopulacao) < (Config.tamanhoPopulacao - Config.qtdIndividuosElitismo):
				# selecione dois individuos
				selecionados = Selecao.torneioBinario(populacao);
				
				# cruzamento
				if Cruzamento.podeCruzar():
					selecionados = Cruzamento.cruzar(selecionados);

				# mutacao
				if Mutacao.podeMutar():
					selecionados = Mutacao.mutar(selecionados)
				
				novaPopulacao.extend(selecionados);
			
			# elitistismo
			melhores = Selecao.melhores(populacao)
			novaPopulacao.extend(melhores)
			
			# avalie todos os individuos
			Fitness.calcularFitness(novaPopulacao)
			
			populacao = []			
			populacao.extend(novaPopulacao)			
			novaPopulacao = []			
			melhores = []

		print('####\n\t\tfim geracoes\n####')

	def rodar(self):
		for i in range(0, Config.qtdIteracoes):
			print('##\n\t\titeracao ' + str(i) + '\n##')
			self.ag()
		print('##\n\t\tfim algoritmo\n##')



Config.geracoes = 10
Config.tamanhoPopulacao = 1000
Config.qtdIteracoes = 1
Config.qtdIndividuosElitismo = 2
Config.taxaCruzamento = 0.80
Config.taxaMutacao = 0.05

Config.classes = 2
Config.numeros = [14,99,110,166,712,760,642,296,113,900,456,358,289,849,137,542,672,247,505,712]

g = Genetico()
g.rodar()