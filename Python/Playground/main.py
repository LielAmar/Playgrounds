import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import sobel
from scipy import ndimage

def calculate_gradient(image):
  # Calculate the gradient using Sobel
  gradient_x = sobel(image, axis=1)
  gradient_y = sobel(image, axis=0)

  # Calculate the magnitude of the gradient
  magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

  # Apply threshold
  threshold = 10
  image = np.where(magnitude < threshold, 0, 1)

  return image

def display(result_image):
  # Display the results
  plt.figure(figsize=(10, 5))

  plt.subplot(1, 2, 1)
  plt.title('Original Image')
  plt.imshow(original_image)
  plt.axis('off')

  plt.subplot(1, 2, 2)
  plt.title('Magnitude Thresholded')
  plt.imshow(result_image, cmap='gray')
  plt.axis('off')

  plt.show()

if __name__ == "__main__":
  image_path = 'test_img1.jpg'
  
  original_image = plt.imread(image_path)

  red1 = calculate_gradient(original_image[:, :, 0])
  green1 = calculate_gradient(original_image[:, :, 1])
  blue1 = calculate_gradient(original_image[:, :, 2])

  # display(red1)
  # display(green1)
  # display(blue1)

  print("red1 - green1", np.sum(np.square(np.abs(red1 - green1))))
  print("red1 - blue1", np.sum(np.square(np.abs(red1 - blue1))))

  # display(red1 - green1)
  # display(red1 - blue1)


  image_path = 'test_img9.jpg'
  
  original_image = plt.imread(image_path)

  red2 = calculate_gradient(original_image[:, :, 0])
  green2 = calculate_gradient(original_image[:, :, 1])
  blue2 = calculate_gradient(original_image[:, :, 2])

  # display(red2)
  # display(green2)
  # display(blue2)

  print("red2 - green2", np.sum(np.square(np.abs(red2 - green2))))
  print("red2 - blue2", np.sum(np.square(np.abs(red2 - blue2))))

  # display(red2 - green2)
  # display(red2 - blue2)

  # display(red)

  print("======")

  print("red1 - green2", np.sum(np.square(np.abs(red1 - green2))))
  print("red1 - blue2", np.sum(np.square(np.abs(red1 - blue2))))

  print("red2 - green1", np.sum(np.square(np.abs(red2 - green1))))
  print("red2 - blue1", np.sum(np.square(np.abs(red2 - blue1))))

  