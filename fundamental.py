# matplolib merupakan sebuah package yang diseadiadakan untuk melakukan penggambaran grafik yang biasanya dikombinasikan dengan package python
# lainnya dalam mempermudah developing data analyst maupun data science

import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[11, 5], [12, 14]])

plt.plot(a, b, c)
plt.show()

# tutorial penggunaan matplotlib adalah
# 1. membuat sebuah data
# 2. membuat sebuah plot
# 3. menampilkan sebuah plot
