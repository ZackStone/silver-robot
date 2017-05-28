import genetico.genetico as genetico

print(genetico)

geracoes = 5
tamanhoPopulacao = 5000
qtdIteracoes = 3
qtdIndividuosElitismo = 2
taxaCruzamento = 0.85
taxaMutacao = 0.05
classes = 2
numeros = [14,99,110,166,712,760,642,296,113,900,456,358,289,849,137,542,672,247,505,712]

solucao = genetico.genetico_run(classes, numeros, geracoes, tamanhoPopulacao, qtdIteracoes, qtdIndividuosElitismo, taxaCruzamento, taxaMutacao)
print(solucao)