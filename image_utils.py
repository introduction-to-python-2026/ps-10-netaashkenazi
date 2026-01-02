from PIL import Image
import numpy as np
from scipy.signal import convolve2d
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image_array = np.array(image)
    return image_array

def edge_detection(image):
    image = np.mean(image, axis=2)
    plt.imshow(image, cmap='gray')
    kernelY = np.array([[1,2,1],
                     [0,  0,  0],
                     [-1,-2,-1]])
    
    kernelX = np.array([[-1, 0, 1],
                     [-2,0,2],
                        [-1,0,1]])
    edgeX = convolve2d(image, kernelX, mode='same')
    edgeY = convolve2d(image, kernelY, mode='same')
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG


binary_image = np.where(image2_copy<60 ,0 ,1)
plt.imsave('my_edges.png', binary_image, cmap='gray')
