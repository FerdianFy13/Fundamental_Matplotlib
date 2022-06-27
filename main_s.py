import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# read image
img = mpimg.imread("stinkbug.png")
print(img)
imgplot = plt.imshow(img)

# schemen image color
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
plt.colorbar()

# plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc="k", ec="k")
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
ax.set_title("Before")
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation="horizontal")
ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
ax.set_title("After")
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation="horizontal")

# showing image in pyplot for matplotlib
plt.show()
