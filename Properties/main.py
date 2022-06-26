import numpy as np
import matplotlib.pyplot as plt


def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = generator(1, 1, 4, 0)
t2, y2 = generator(1, 1, 4, 90)
t3, y3 = generator(1, 1, 4, 180)

dataplot1 = plt.plot(t1, y1)
dataplot2 = plt.plot(t2, y2)
dataplot3 = plt.plot(t3, y3)

# set property yang digunakn untuk mengatur property dari plot
plt.setp(dataplot1, color="r", linestyle="-", linewidth=1)
plt.setp(dataplot2, color="g", linestyle="-.", linewidth=2.25)
plt.setp(dataplot3, color="b", linestyle="--", linewidth=1.5)

plt.show()

x = "Python"
y = [1, 2, 3]

z = x, y
# print(z[1][1:])
