import numpy as np
import random

def funcao(r, t):
    # A função foi tranformada para coordenadas polares
    return 2*((4-r**2)*np.sqrt(3)*r**2)

# limites de integracao de r
lInferiorR = 0
lSuperiorR = 2

# limites de integracao de theta
lInferiorTheta = 0
lSuperiorTheta = 2*np.pi

# numero de iteracoes (pontos)
n = 1000000

# guarda o valor do somatorio dos pontos aleatorios
soma = 0

for i in range(n):
    # gera um valor aleatorio entre os limites de integracao de r
    aleatorioR = random.uniform(lInferiorR, lSuperiorR)

    # desnecessario pois a funcao nao depende de theta
    aleatorioTheta = random.uniform(lInferiorTheta, lSuperiorTheta)

    # somatorio dos valores aleatorios da funcao
    soma += funcao(aleatorioR, aleatorioTheta)

print(soma/n*(lSuperiorR-lInferiorR)*(lSuperiorTheta-lInferiorTheta))