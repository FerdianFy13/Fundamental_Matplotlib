# matplolib merupakan sebuah package yang diseadiadakan untuk melakukan penggambaran grafik yang biasanya dikombinasikan dengan package python
# lainnya dalam mempermudah developing data analyst maupun data science

import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

plt.plot(a, b)
plt.show()
