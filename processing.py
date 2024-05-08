import cv2
import matplotlib.pyplot as plt
import os
import price

# Read the image
img = cv2.imread('images/image3.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the enhanced image to a file
enhanced_img_path = 'enhanced_image.jpg'
cv2.imwrite(enhanced_img_path, gray_img)

# Display the original and enhanced images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB))
plt.title('Original Image')
plt.axis('off')

# Call the text extraction function from the price module with the file path of the enhanced image
price.textextract(enhanced_img_path)

# Apply contrast enhancement using histogram equalization
enhanced_img = cv2.equalizeHist(gray_img)

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(enhanced_img, cv2.COLOR_GRAY2RGB))
plt.title('Enhanced Image')
plt.axis('off')

plt.show()


# Perform OCR on the preprocessed image
price.textextract(gray_img)

# Apply contrast enhancement using histogram equalization
enhanced_img = cv2.equalizeHist(gray_img)

# Display the enhanced image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(enhanced_img, cv2.COLOR_GRAY2RGB))
plt.title('Enhanced Image')
plt.axis('off')

plt.show()
