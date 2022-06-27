import numpy as np
import matplotlib.pyplot as plt


def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = generator(1, 1, 4, 0)

plt.plot(t1, y1, "r-o")
plt.text(2, 0.8, "sin(90)")

plt.show()
