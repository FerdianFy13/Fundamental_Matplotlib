import numpy as np
import matplotlib.pyplot as plt


def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


judul = "Grafik Sinusoidal\n"
rumus = r"$ \mathcal{Y}  = A.sin(2 \omega t + \theta)$" + "\n"
parameter1 = r"$ A = $" + str(1) + " cm, "
parameter2 = r"$ \omega = $" + str(1) + r"$ \mathit{Hz}$" + ", "
parameter3 = r"$ \theta = $" + str(0) + r"$^{o} $"

t1, y1 = generator(1, 1, 4, 0)

plt.plot(t1, y1, "r-o")
plt.axis([0, 4, -1, 1])
plt.xlabel("time(second)")
plt.ylabel("amplitudo(frecuency)")
plt.title(judul + rumus + parameter1 + parameter2 + parameter3)

plt.show()
