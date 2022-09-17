import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

x = np.array([0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999])
mylabels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mycolors = ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]

plt.pie(x, labels = mylabels, startangle = 105, colors = mycolors)
plt.show()