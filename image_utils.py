image_path = r"/content/gallery_Party_Party_113.jpg"
image1 = load_image(image_path)

from skimage.filters import median
from skimage.morphology import ball

clean_image = median(image1, ball(3))



image2 = edge_detection(clean_image)
image2_copy = image2.copy()
from PIL import Image
from matplotlib import pyplot as plt

plt.figure(figsize=(3,2))
plt.hist(image2_copy.flatten(), bins =256);
plt.show()

binary_image = np.where(image2_copy<60 ,0 ,1)
edge_image = plt.imshow(binary_image, cmap='gray')
plt.imsave('my_edges.png', binary_image, cmap='gray')
