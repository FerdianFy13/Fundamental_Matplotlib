import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(sudut))


# membuat plot

plt.plot(sudut, y, "r-o")
plt.title("grafik sinusoidal")
plt.text(190, 1, "magnituda")
plt.text(360, 0.1, "sudut")
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xticks(
    [0, 90, 180, 270, 360],
    [r"${0}^o$", r"${90}^o$", r"${180}^o$", r"${270}^o$", r"${360}^o$"],
)

# gca or get current axis digunakan untuk merubah tata letak dari posisi asli axis sebenernya yang diubah sesuai dengan kebutuhan data yang dibutuhkan
ax = plt.gca()
ax.spines["left"].set_position(("data", 180))
ax.spines["bottom"].set_position(("data", 0))
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")


# tampilkan
plt.show()
