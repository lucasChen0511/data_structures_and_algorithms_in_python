import matplotlib.pyplot as plt
import numpy as np
import math

x = [x/100 for x in range(1, 500)]
y1 = list(map(lambda x : 4 * math.log(x), x))
y2 = x

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()