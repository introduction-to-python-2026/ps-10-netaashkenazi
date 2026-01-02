from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image_array = np.array(image)
    return image_array


def edge_detection(image_array):
    image_array = np.mean(image_array, axis=2)
    plt.imshow(image_array, cmap='gray')
    kernelY = np.array([[1,2,1],
                     [0,  0,  0],
                     [-1,-2,-1]])
    
    kernelX = np.array([[-1, 0, 1],
                     [-2,0,2],
                        [-1,0,1]])
    edgeX = convolve2d(image_array, kernelX, mode='same')
    edgeY = convolve2d(image_array, kernelY, mode='same')
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG
