import numpy as np
import matplotlib.pyplot as plt

def init(q1, q2, dx, jmax):
    xs = -1.0
    x = np.linspace(xs, xs+dx*(jmax-1), jmax)
    q = np.array([(float(q1) if i<0.0 else float(q2)) for i in x])
    return (x, q)

def do_computing(x, q, dt, dx, nmax, ff, order=1, interval=2):
    plt.figure(figsize=(7,7), dpi=100)
    plt.rcParams["font.size"] = 22

    plt.plot(x, q, marker='o', lw=2, label='n=0')

    for n in range(1, nmax+1):
        qold = q.copy()
        for j in range(order, jmax-order):
            ff1 = ff(qold, qold[j], dt, dx, j)
            ff2 = ff(qold, qold[j], dt, dx, j-1)
            q[j] = qold[j] - dt/dx * (ff1 - ff2)
            
        if n % interval == 0:
            plt.plot(x, q, marker='o', lw=2, label=f'n={n}')
            
    plt.grid(color='black', linestyle='dashed', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('q')
    plt.legend()
    #plt.show()
    plt.savefig('output_plot.png')

def MC(q, c, dt, dx, j):
    ur = q[j+1]
    ul = q[j]
    fr = 0.5 * ur**2
    fl = 0.5 * ul**2
    c = 0.5 * (ur + ul)
    return 0.5 * (fr + fl - np.sign(c) * (fr - fl))

### This function doesn't use if else structure
def GODUNOV(q, c, dt, dx, j):
    qm = 0.5 * (q[j] + np.abs(q[j]))
    qp = 0.5 * (q[j+1] - np.abs(q[j+1]))
    return np.max([0.5 * qm**2, 0.5 * qp**2])
    

c = 1
dt = 0.05
dx = 0.1

jmax = 21
nmax = 10

q1 = -1
q2 = 1
x, q = init(q1, q2, dx, jmax)
do_computing(x, q, dt, dx, nmax, GODUNOV, interval=2)
