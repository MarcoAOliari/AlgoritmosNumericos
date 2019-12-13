import numpy as np
import random

def funcao(r, t):
    # A função foi tranformada para coordenadas polares
    return 2*((4-r**2)*np.sqrt(3)*r**2)

def umTerco2D(n, h1, h2, lInferiorR, lInferiorTheta):
    integral = 0
    for i in range(0, n-1, 2):
        for j in range(0, n-1, 2):
            integral += 2*(h2)*2*(h1)*(funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            4*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)))/6

    return integral

def tresOitavos2D(n, h1, h2, lInferiorR, lInferiorTheta):
    integral = 0
    for i in range(0, n-1, 3):
        for j in range(0, n-1, 3):
            integral += 3*h1*3*h2*(funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            3*funcao(lInferiorR + h1*(j+1), lInferiorTheta + (h1*(j+1))) +
            3*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            funcao(lInferiorR + h1*(j+3),lInferiorTheta + h1*(j+3)))/8

    return integral

def regraDeBoole(n, h1, h2, lInferiorR, lInferiorTheta):
    integral = 0
    for i in range(0, n-1, 4):
        for j in range(0, n-1, 4):
            integral += 4*h1*4*h2*(7*funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            32*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            12*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            32*funcao(lInferiorR + h1*(j+3), lInferiorTheta + h1*(j+3)) +
            7*funcao(lInferiorR + h1*(j+4), lInferiorTheta + h1*(j+4)))/90

    return integral

def regraSeisPontos(n, h1, h2, lInferiorR, lInferiorTheta):
    integral = 0
    for i in range(0, n-1, 5):
        for j in range(0, n-1, 5):
            integral += 5*h1*5*h2*(19*funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            75*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            50*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            50*funcao(lInferiorR + h1*(j+3), lInferiorTheta + h1*(j+3)) +
            75*funcao(lInferiorR + h1*(j+4), lInferiorTheta + h1*(j+4)) +
            19*funcao(lInferiorR + h1*(j+5), lInferiorTheta + h1*(j+5)))/288

    return integral


# limites de integracao de r
lInferiorR = 0
lSuperiorR = 2

# limites de integracao de theta
lInferiorTheta = 0
lSuperiorTheta = 2*np.pi

# numero de pontos
# para maior precisao:
# para 1/3, (n-1) divisivel por 2
# para 3/8, (n-1) divisivel por 3
# para boole, (n-1) divisivel por 4
# para 6 pontos, (n-1) divisivel por 5
n = 901

h1 = (lSuperiorR - lInferiorR)/(n-1)
h2 = (lSuperiorTheta - lInferiorTheta)/(n-1)

print(umTerco2D(n, h1, h2, lInferiorR, lInferiorTheta))
print(tresOitavos2D(n, h1, h2, lInferiorR, lInferiorTheta))
print(regraDeBoole(n, h1, h2, lInferiorR, lInferiorTheta))
print(regraSeisPontos(n, h1, h2, lInferiorR, lInferiorTheta))

