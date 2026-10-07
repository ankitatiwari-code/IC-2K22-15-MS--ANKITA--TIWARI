import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\JSK\OneDrive\Desktop\multimediaLab\IC-2K22-15-MS- ANKITA -TIWARI\datasets\IMG_20200616_152325 - Copy.jpg"
)

if img is None:
    print("Error: image was not found.")
else:
    # BGR order, not RGB
    print("shape:", img.shape)

    # uint8 → values 0..255
    print("dtype:", img.dtype)

    print("min/max:", img.min(), img.max())

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("gray shape:", gray.shape)

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Original")

    # Display grayscale image
    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.axis("off")
    plt.title("Grayscale")

    plt.show()