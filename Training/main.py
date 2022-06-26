import numpy as np
import matplotlib.pyplot as plt


def generator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = generator(1, 1, 4, 0)
t2, y2 = generator(1, 1, 4, 90)

# fungsi figure digunakan semacam container yang menampilkan layer tersebut sesuai number yang dimasukkan oleh si user ketika melakukan visualisasi sebuah data
plt.figure(2)
# sub plot merupakan sebuah angka atau number dari axis dari layer container yang menyesuaikan dengan visualisasi data yang dimasukkan oleh si user
ax = plt.subplot(111)

plt.plot(t1, y1, "r-o", label="sin(0)")
plt.plot(t2, y2, "g-o", label="sin(90)")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])

# fungsi dari legend adalah digunakan untuk mencocokkan antara label dengan garis warna dari data yang dimasukkan untuk menghasilkan sebuah data yang baru
plt.legend(loc="upper center", bbox_to_anchor=(1.2, 1))

plt.show()
