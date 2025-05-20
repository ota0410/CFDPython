import numpy as np
import matplotlib.pyplot as plt

c = 1
dt = 0.025
dx = 0.05

jmax = 20*2+1
nmax = 6*2

x = np.linspace(0, dx * (jmax-1), jmax)
q = np.zeros(jmax)

for j in range(jmax):
    if(j < jmax/2):
        q[j] = 1
    else:
        q[j] = 0

plt.figure(figsize=(7,7), dpi=100)
plt.rcParams["font.size"]

plt.plot(x, q, marker='o', lw=2, label='n=0')

for n in range(1, nmax+1):
    qold = q.copy()
    for j in range(1, jmax-1):
        q[j] = qold[j] - dt * c * (qold[j] - qold[j-1])/dx

    if n%2 == 0:
        plt.plot(x, q, marker='o', lw=2, label=f'n={n}')

plt.grid(color='black', linestyle='dashed', linewidth=0.5)
plt.xlim([0,2.0])
plt.xlabel('x')
plt.ylabel('q')
plt.legend()
plt.show()
