import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import os


# --------------------------------------------------
# 1. Create output folder
# --------------------------------------------------

os.makedirs("output", exist_ok=True)


# --------------------------------------------------
# 2. Read the input image
# --------------------------------------------------

input_path = "datasets/photo.jpg"

image = cv2.imread(input_path)

if image is None:
    print("Error: Image not found.")
    print("Please check the path:", input_path)
    exit()

print("Image loaded successfully.")


# --------------------------------------------------
# 3. Convert BGR to RGB
# --------------------------------------------------

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# --------------------------------------------------
# 4. Convert image to grayscale
# --------------------------------------------------

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output/grayscale.jpg", gray_image)

print("Grayscale image saved.")


# --------------------------------------------------
# 5. Brightness Enhancement
# --------------------------------------------------

pil_image = Image.open(input_path)

brightness_enhancer = ImageEnhance.Brightness(pil_image)

bright_image = brightness_enhancer.enhance(1.5)

bright_image.save("output/brightness_enhanced.jpg")

print("Brightness enhanced image saved.")


# --------------------------------------------------
# 6. Contrast Enhancement
# --------------------------------------------------

contrast_enhancer = ImageEnhance.Contrast(pil_image)

contrast_image = contrast_enhancer.enhance(1.5)

contrast_image.save("output/contrast_enhanced.jpg")

print("Contrast enhanced image saved.")


# --------------------------------------------------
# 7. Sharpness Enhancement
# --------------------------------------------------

sharpness_enhancer = ImageEnhance.Sharpness(pil_image)

sharp_image = sharpness_enhancer.enhance(2.0)

sharp_image.save("output/sharpness_enhanced.jpg")

print("Sharpness enhanced image saved.")


# --------------------------------------------------
# 8. Histogram Equalization
# --------------------------------------------------

equalized_image = cv2.equalizeHist(gray_image)

cv2.imwrite(
    "output/histogram_equalized.jpg",
    equalized_image
)

print("Histogram equalized image saved.")


# --------------------------------------------------
# 9. CLAHE Enhancement
# --------------------------------------------------

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

clahe_image = clahe.apply(gray_image)

cv2.imwrite(
    "output/clahe_enhanced.jpg",
    clahe_image
)

print("CLAHE enhanced image saved.")


# --------------------------------------------------
# 10. Sharpening using Kernel
# --------------------------------------------------

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(
    image,
    -1,
    kernel
)

cv2.imwrite(
    "output/kernel_sharpened.jpg",
    sharpened
)

print("Kernel sharpened image saved.")


# --------------------------------------------------
# 11. Create Comparison Figure
# --------------------------------------------------

plt.figure(figsize=(15, 10))


# Original
plt.subplot(3, 3, 1)
plt.imshow(rgb_image)
plt.title("Original Image")
plt.axis("off")


# Grayscale
plt.subplot(3, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale")
plt.axis("off")


# Brightness
plt.subplot(3, 3, 3)
plt.imshow(bright_image)
plt.title("Brightness Enhanced")
plt.axis("off")


# Contrast
plt.subplot(3, 3, 4)
plt.imshow(contrast_image)
plt.title("Contrast Enhanced")
plt.axis("off")


# Sharpness
plt.subplot(3, 3, 5)
plt.imshow(sharp_image)
plt.title("Sharpness Enhanced")
plt.axis("off")


# Histogram Equalization
plt.subplot(3, 3, 6)
plt.imshow(equalized_image, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")


# CLAHE
plt.subplot(3, 3, 7)
plt.imshow(clahe_image, cmap="gray")
plt.title("CLAHE")
plt.axis("off")


# Kernel Sharpening
plt.subplot(3, 3, 8)
plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.title("Kernel Sharpening")
plt.axis("off")


plt.tight_layout()

plt.savefig(
    "output/comparison.jpg",
    dpi=300
)

plt.show()

print("\nAll image enhancement operations completed.")
print("Check the output folder.")