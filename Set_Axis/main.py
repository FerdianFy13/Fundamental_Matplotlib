import numpy as np
import matplotlib.pyplot as plt

# axis merupakan sebuah garis x dan y dalam sebuah grafif yang menyesuaikan dengan data yang dibutuhkan
def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = generator(1, 1, 4, 0)

plt.plot(t1, y1, "r-o")

# mengatur nilai minimum dan maximum dari axis alignment
# sehingga user dapatt menentukan nilai minimum dan maximum dari garis yang akan dibentuk dalam linear propertynya
plt.axis([0, 4, -2, 2])

plt.show()
