import numpy as np
import matplotlib.pyplot as plt

corner = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(corner))

plt.plot(corner, y)

# fungsi ticcks digunakan untuk mengatur jumlah data dalam axis pada data disesuaikan dengan data yang dibutuhkan oleh masing-masing user ketika menggunakan pyplot dalam menghasilkan sebuah data baru
plt.yticks([-1, 0, 1])
plt.xticks([0, 90, 180, 270, 360])

plt.show()
