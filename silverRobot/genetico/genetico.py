from .config import Config
from .individuo import Individuo
from .populacao import Populacao
from .cruzamento import Cruzamento
from .mutacao import Mutacao
from .selecao import Selecao
from .fitness import Fitness
import copy

class Genetico:

	individuos = []
	solucao = None

	def __init__(self, individuos=[]):
		self.individuos = individuos

	def ag(self):
		#print('####\n\t\tpopulacao inicial\n####')
		populacao = Populacao.gerarPopulacaoInicial()
		populacao = Fitness.calcularFitness(populacao)

		novaPopulacao = []
		# ate que o numero de geracoes finalize
		for i in range(0, Config.geracoes):
			#print('####\n\t\tgeracao ' + str(i) + '\n####')
			
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
			novaPopulacao = Fitness.calcularFitness(novaPopulacao)
			
			###################################
			melhor = Selecao.melhor(populacao)
			melhor = Fitness.calcularFitness([melhor])[0]
			if self.solucao == None or melhor.fitness < self.solucao.fitness:
				self.solucao = copy.deepcopy(melhor)
			###################################


			populacao = []			
			populacao.extend(novaPopulacao)			
			novaPopulacao = []			
			melhores = []

		#print('####\n\t\tfim geracoes\n####')

def genetico_run(classes, numeros, geracoes, tamanhoPopulacao, qtdIteracoes, qtdIndividuosElitismo, taxaCruzamento, taxaMutacao):

	Config.geracoes = geracoes
	Config.tamanhoPopulacao = tamanhoPopulacao
	Config.qtdIteracoes = qtdIteracoes
	Config.qtdIndividuosElitismo = qtdIndividuosElitismo
	Config.taxaCruzamento = taxaCruzamento
	Config.taxaMutacao = taxaMutacao
	Config.classes = classes
	Config.numeros = numeros

	g = Genetico()

	for i in range(0, Config.qtdIteracoes):
		#print('##\n\t\titeracao ' + str(i) + '\n##')
		g.ag()
	#print('##\n\t\tfim algoritmo\n##')
	#print(g.solucao)
	return g.solucao