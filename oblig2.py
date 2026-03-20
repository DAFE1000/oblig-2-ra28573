import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve 


#Funksjon
def f(x):
    return np.exp(-x/4) * np.arctan(x)


#ligningen som bestemmer toppunktet:
def g(x):
    return np.arctan(x) - 4/(x**2 +1)

#Finn nullpunkt nummerisk
x_topp = fsolve(g, 1.7)[0]
y_topp = f(x_topp)


print(f"x_topp = {x_topp:.6f}")
print(f"y_topp = {y_topp:.6f}")


#plot
x = np.linspace(-4, 10, 500)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label=r'$f(x)=e^{-x/4}\arctan(x)$')
plt.plot(x_topp, y_topp, 'ro' , label=f'Toppunkt ({x_topp:.4f}, {y_topp:.4f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot av funksjonen med toppunkt')
plt.grid(True)
plt.legend()
plt.show()