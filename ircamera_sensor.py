# smart-home controller code
# started: 4/16/2019
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import glob
from skimage.io import imread

ex_image = glob.glob(r"‪C:/Users/EliPl/Downloads/IMG_0791.JPG")[0]
im=imread(ex_image, as_gray=True)
plt.imshow(im, cmap=cm.gray)
plt.show()