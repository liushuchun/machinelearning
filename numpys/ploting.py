import numpy as np
import matplotlib
import matplotlib.pyplot as plt
X = np.linspace(-4,4,1000)

Y= X**2

plt.plot(X,Y,'r')
Ints =np.arange(-4,5)
plt.plot(Ints, Ints**2,'bo')

plt.savefig("simple.pdf")

