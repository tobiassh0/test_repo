import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = x**2
plt.plot(x,y,'-b')
plt.xlabel('x') ; plt.ylabel('y')
plt.savefig('quadratic.png')

