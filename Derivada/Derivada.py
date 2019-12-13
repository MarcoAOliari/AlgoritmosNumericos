import numpy as np

def funcao(x):
    return np.exp(x)

def fLinha5Pts(n, k, coluna_b, coeficientes):
    j = 0
    fLinha = np.zeros((n, 1))

    for i in range(n):
        if i < 2:
            fLinha[i] = k*np.dot(coluna_b[0:5].transpose(), coeficientes[j])
            j += 1
        elif i < n-2:
            fLinha[i] = k*np.dot(coluna_b[i-2:i+3].transpose(), coeficientes[j])
        else:
            j += 1
            fLinha[i] = k*np.dot(coluna_b[n-5:n].transpose(), coeficientes[j])

    return fLinha

def fLinha7Pts(n, k, coluna_b, coeficientes):
    j = 0
    fLinha = np.zeros((n, 1))

    for i in range(n):
        if i < 3:
            fLinha[i] = k*np.dot(coluna_b[0:7].transpose(), coeficientes[j])
            j += 1
        elif i < n-3:
            fLinha[i] = k*np.dot(coluna_b[i-3:i+4].transpose(), coeficientes[j])
        else:
            j += 1
            fLinha[i] = k*np.dot(coluna_b[n-7:n].transpose(), coeficientes[j])

    return fLinha


def primeira5Pts(h, n, coluna_b):
    coeficientes = np.array([[-25, 48, -36, 16, -3],
                             [-3, -10, 18, -6, 1],
                             [1, -8, 0, 8, -1],
                             [-1, 6, -18, 10, 3],
                             [3, -16, 36, -48, 25]])

    k = 1/(12*h)

    return fLinha5Pts(n, k, coluna_b, coeficientes)

def primeira7Pts(h, n, coluna_b):
    coeficientes = np.array([[-294, 720, -900, 800, -450, 144, -20],
                             [-20, -154, 300, -200, 100, -30, 4],
                             [4, -48, -70, 160, -60, 16, -2],
                             [-2, 18, -90, 0, 90, -18, 2],
                             [2, -16, 60, -160, 70, 48, -4],
                             [-4, 30, -100, 200, -300, 154, 20],
                             [20, -144, 450, -800, 900, -720, 294]])

    k = 1/(120*h)
    fLinha = np.zeros((n, 1))
    j = 0

    return fLinha7Pts(n, k, coluna_b, coeficientes)

def segunda5Pts(h, n, coluna_b):
    coeficientes = np.array([[35, -104, 114, -56, 11],
                             [11, -20, 6, 4, -1],
                             [-1, 16, -30, 16, -1],
                             [-1, 4, 6, -20, 11],
                             [11, -56, 114, -104, 35]])

    k = 1/(12*h**2)

    return fLinha5Pts(n, k, coluna_b, coeficientes)

def segunda7Pts(h, n, coluna_b):
    coeficientes = np.array([[812, -3132, 5265, -5080, 2970, -972, 137],
                             [137, -147, -255, 470, -285, 93, -13],
                             [-13, 228, -420, 200, 15, -12, 2],
                             [2, -27, 270, -490, 270, -27, 2],
                             [2, -12, 15, 200, -420, 228, -13],
                             [-13, 93, -285, 470, -255, -147, 137],
                             [137, -972, 2970, -5080, 5265, -3132, 812]])

    k = 1/(180*h**2)

    return fLinha7Pts(n, k, coluna_b, coeficientes)

def terceira(h, n, coluna_b):
    coeficientes = np.array([[-49, 232, -461, 496, -307, 104, -15],
                             [-15, 56, -83, 64, -29, 8, -1],
                             [-1, -8, 35, -48, 29, -8, 1],
                             [1, -8, 13, 0, -13, 8, -1],
                             [-1, 8, -29, 48, -35, 8, 1],
                             [1, -8, 29, -64, 83, -56, 15],
                             [15, -104, 307, -496, 461, -232, 49]])

    k = 1/(8*h**3)

    return fLinha7Pts(n, k, coluna_b, coeficientes)

def quarta(h, n, coluna_b):
    coeficientes = np.array([[35, -186, 411, -484, 321, -114, 17],
                             [17, -84, 171, -184, 111, -36, 5],
                             [5, -18, 21, -4, -9, 6, -1],
                             [-1, 12, -39, 56, -39, 12, -1],
                             [-1, 6, -9, -4, 21, -18, 5],
                             [5, -36, 111, -184, 171, -84, 17],
                             [17, -114, 321, -484, 411, -186, 35]])

    k = 1/(6*h**4)

    return fLinha7Pts(n, k, coluna_b, coeficientes)

n = 21
coluna_b = np.zeros((n, 1))

lInferior = -2
lSuperior = 2

h = (lSuperior-lInferior)/(n-1)

id = 4

for i in range(n):
    coluna_b[i] = funcao(lInferior + i*h)

if id == 0:
    resposta = (primeira5Pts(h, n, coluna_b))
elif id == 1:
    resposta = (primeira7Pts(h, n, coluna_b))
elif id == 2:
    resposta = (segunda5Pts(h, n, coluna_b))
elif id == 3:
    resposta = (segunda7Pts(h, n, coluna_b))
elif id == 4:
    resposta = (terceira(h, n, coluna_b))
else:
    resposta = (quarta(h, n, coluna_b))

erro = np.zeros((n, 1))
erroMedio = 0

for i in range(n):
    erro[i] = np.abs((resposta[i] - coluna_b[i])/coluna_b[i] * 100)
    erroMedio += erro[i]/n

print("Derivada:")
print(resposta)
print("Erros:")
print(erro, "\n")
print("Erro Médio: %f%%" %erroMedio)
print("Maior Erro: %f%%" %max(erro))
