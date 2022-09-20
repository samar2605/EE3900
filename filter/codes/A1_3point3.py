import matplotlib.pyplot as plt
import numpy as np

y = np.loadtxt("Y.dat",dtype = "double")
x = np.array([1,2,3,4,2,1])

# ploting graph
#subplot for x(n)
plt.subplot(211)
plt.stem(np.arange(len(x)),x)
plt.xlabel("n")
plt.ylabel("$x(n)$")
plt.grid()

#subplot for y(n)
plt.subplot(212)
plt.stem(np.arange(len(y)),y)
plt.xlabel("n")
plt.ylabel("$y(n)$")
plt.grid()

#plot fig output
plt.show()