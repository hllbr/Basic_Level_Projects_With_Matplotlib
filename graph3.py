import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = np.arange(2,11,2)

fig = plt.figure()


axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1 = fig.add_axes([0.4,0.5,0.4,0.3])


plt.show()
