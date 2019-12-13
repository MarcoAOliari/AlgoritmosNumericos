import matplotlib.pyplot as plt
from matplotlib import style

def fx(coef, t, x, y, z):
    return coef[0]*x - coef[1]*x*y

def fy(coef, t, x, y, z):
    return -coef[2]*y + coef[1]*x*y - coef[4]*y*z

def fz(coef, t, x, y, z):
    return -coef[5]*z + coef[6]*y*z

#Metodo de Runge Kutta de quarta ordem
def RK4(coef, inicio, x, y, z, h):
    k0 = h * fx(coef, inicio, x, y, z)
    l0 = h * fy(coef, inicio, x, y, z)
    m0 = h * fz(coef, inicio, x, y, z)

    k1 = h * fx(coef, inicio + 1/2*h, x + 1/2*k0, y + 1/2*l0, z + 1/2*m0)
    l1 = h * fy(coef, inicio + 1/2*h, x + 1/2*k0, y + 1/2*l0, z + 1/2*m0)
    m1 = h * fz(coef, inicio + 1/2*h, x + 1/2*k0, y + 1/2*l0, z + 1/2*m0)

    k2 = h * fx(coef, inicio + 1/2*h, x + 1/2*k1, y + 1/2*l1, z + 1/2*m1)
    l2 = h * fy(coef, inicio + 1/2*h, x + 1/2*k1, y + 1/2*l1, z + 1/2*m1)
    m2 = h * fz(coef, inicio + 1/2*h, x + 1/2*k1, y + 1/2*l1, z + 1/2*m1)

    k3 = h * fx(coef, inicio + h, x + k2, y + l2, z + m2)
    l3 = h * fy(coef, inicio + h, x + k2, y + l2, z + m2)
    m3 = h * fz(coef, inicio + h, x + k2, y + l2, z + m2)

    x = x + 1/6*(k0 + 2*k1 + 2*k2 + k3)
    y = y + 1/6*(l0 + 2*l1 + 2*l2 + l3)
    z = z + 1/6*(m0 + 2*m1 + 2*m2 + m3)

    return x, y, z

coef = [1, 1, 1, 1, 1, 1, 1]

x = 1.2 #cores azul escuro e roxo
y = 1.8 #cores verde e amarelo
z = 2.4 #cores vermelho e azul claro
h = 0.05
inicio = 0
fim = 10
passo = 0
vecx = []
vecy = []
vecz = []
vecpasso = []

style.use('seaborn-pastel')

#calcula os valores de x y e z com o tempo e plota em cada loop
for j in range(int(fim/h)):
    plt.scatter(passo, x)
    plt.scatter(passo, y)
    plt.scatter(passo, z)
    plt.pause(0.1)
    x, y, z = RK4(coef, inicio, x, y, z, h)
    passo += h

plt.show()

#para condicoes iniciais 1 1 1 percebe-se uma linha central no grafico que representa o teto de uma especie (z) e o piso
#de outra (x), em que em determinado momento os graficos tangenciam ao mesmo tempo.

#com y igual a 0, z tende a 0 exponencialmente e x cresce exponencialmente, tendendo ao infinito.

#com x igual a 0, y e z tendem a 0.



