from scipy import ndimage
from scipy import misc
import pylab as pl
import matplotlib.pyplot as	plt
import numpy as	np

def main():
    img = misc.imread('../Data/lena.jpg', mode = 'L')

    # Flip the image
    flip_lena = np.flipud(img)

    # Tansfer the image into grayscale
    plt.imshow(flip_lena, cmap = plt.cm.gray)

    # Print the image
    plt.show()


if __name__ == '__main__':
    main()