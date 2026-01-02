from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
from matplotlib import pyplot as plt


image_path = r"/content/gallery_Party_Party_113.jpg"
image1 = load_image(image_path)

from skimage.filters import median
from skimage.morphology import ball

clean_image = median(image1, ball(3))



image2 = edge_detection(clean_image)
image2_copy = image2.copy()
from PIL import Image
from matplotlib import pyplot as plt
binary_image = np.where(image2_copy<60 ,0 ,1)
edge_image = plt.imshow(binary_image, cmap='gray')
plt.imsave('my_edges.png', binary_image, cmap='gray')
