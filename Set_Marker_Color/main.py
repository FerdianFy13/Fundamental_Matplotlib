import numpy as np
import matplotlib.pyplot as plt


def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = generator(1, 1, 4, 0)
t2, y2 = generator(1, 1, 4, 90)
t3, y3 = generator(1, 1, 4, 60)
t4, y4 = generator(1, 1, 4, 90)

plt.plot(t1, y1, "r")
plt.plot(t2, y2, "g")
plt.plot(t3, y3, "b--")
plt.plot(t4, y4, "y-o")

plt.show()

# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline
