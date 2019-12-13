import matplotlib.pyplot as plt

def fx(coef, t, x, y, z):
    return coef[0]*x - coef[1]*x*y

def fy(coef, t, x, y, z):
    return -coef[2]*y + coef[1]*x*y - coef[4]*y*z

def fz(coef, t, x, y, z):
    return -coef[5]*z + coef[6]*y*z

def RKF5(coef, inicio, x, y, z, h):
    k0 = h * fx(coef, inicio, x, y, z)
    l0 = h * fy(coef, inicio, x, y, z)
    m0 = h * fz(coef, inicio, x, y, z)

    k1 = h * fx(coef, inicio + 1/4*h, x + 1/4*k0, y + 1/4*l0, z + 1/4*m0)
    l1 = h * fy(coef, inicio + 1/4*h, x + 1/4*k0, y + 1/4*l0, z + 1/4*m0)
    m1 = h * fz(coef, inicio + 1/4*h, x + 1/4*k0, y + 1/4*l0, z + 1/4*m0)

    k2 = h * fx(coef, inicio + 3/8*h, x + 3/32*k0 + 9/32*k1, y + 3/32*l0 + 9/32*l1, z + 3/32*m0 + 9/32*m1)
    l2 = h * fy(coef, inicio + 3/8*h, x + 3/32*k0 + 9/32*k1, y + 3/32*l0 + 9/32*l1, z + 3/32*m0 + 9/32*m1)
    m2 = h * fz(coef, inicio + 3/8*h, x + 3/32*k0 + 9/32*k1, y + 3/32*l0 + 9/32*l1, z + 3/32*m0 + 9/32*m1)

    k3 = h * fx(coef, inicio + 12/13*h, x + 1932/2197*k0 - 7200/2197*k1 + 7296/2197*k2, y + 1932/2197*l0 - 7200/2197*l1 + 7296/2197*l2, z + 1932/2197*m0 - 7200/2197*m1 + 7296/2197*m2)
    l3 = h * fy(coef, inicio + 12/13*h, x + 1932/2197*k0 - 7200/2197*k1 + 7296/2197*k2, y + 1932/2197*l0 - 7200/2197*l1 + 7296/2197*l2, z + 1932/2197*m0 - 7200/2197*m1 + 7296/2197*m2)
    m3 = h * fz(coef, inicio + 12/13*h, x + 1932/2197*k0 - 7200/2197*k1 + 7296/2197*k2, y + 1932/2197*l0 - 7200/2197*l1 + 7296/2197*l2, z + 1932/2197*m0 - 7200/2197*m1 + 7296/2197*m2)

    k4 = h * fx(coef, inicio + h, x + 439/216*k0 - 8*k1 + 3680/513*k2 - 845/4104*k3, y + 439/216*l0 - 8*l1 + 3680/513*l2 - 845/4104*l3, z + 439/216*m0 - 8*m1 + 3680/513*m2 - 845/4104*m3)
    l4 = h * fy(coef, inicio + h, x + 439/216*k0 - 8*k1 + 3680/513*k2 - 845/4104*k3, y + 439/216*l0 - 8*l1 + 3680/513*l2 - 845/4104*l3, z + 439/216*m0 - 8*m1 + 3680/513*m2 - 845/4104*m3)
    m4 = h * fz(coef, inicio + h, x + 439/216*k0 - 8*k1 + 3680/513*k2 - 845/4104*k3, y + 439/216*l0 - 8*l1 + 3680/513*l2 - 845/4104*l3, z + 439/216*m0 - 8*m1 + 3680/513*m2 - 845/4104*m3)

    x = x + 25/216*k0 + 1408/2565*k2 + 2197/4104*k3 - 1/5*k4
    y = y + 25/216*l0 + 1408/2565*l2 + 2197/4104*l3 - 1/5*l4
    z = z + 25/216*m0 + 1408/2565*m2 + 2197/4104*m3 - 1/5*m4

    return x, y, z

coef = [1, 1, 1, 1, 1, 1, 1]

x = 1.2
y = 1.8
z = 2.4
h = 0.001
inicio = 0
fim = 10
passo = 0

vecx = []
vecy = []
vecz = []
vecpasso = []


for i in range(int(fim/h)):
    vecx.append(x)
    vecy.append(y)
    vecz.append(z)
    vecpasso.append(passo)
    x, y, z = RKF4(coef, inicio, x, y, z, h)
    passo += h

plt.plot(vecpasso, vecx)
plt.plot(vecpasso, vecy)
plt.plot(vecpasso, vecz)

plt.show()
