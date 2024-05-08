import pytesseract
from PIL import Image
import numpy as np
import cv2
myconfig = r'--psm 11 --oem 3'
# Open an image file
filename  = 'images/Amul-Milk.jpeg'
image = np.array(Image.open(filename))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use pytesseract to extract text from the image
extracted_data = pytesseract.image_to_data(gray_image, config=myconfig)

extracted_text = pytesseract.image_to_string(gray_image, config=myconfig)

# Print the extracted text
for i, line in enumerate(extracted_data.splitlines()):
    if i == 0:
        continue
    data = line.split('\t')
    if len(data) == 12:
        x, y, w, h = int(data[6]), int(data[7]), int(data[8]), int(data[9])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Print the extracted text
print(extracted_text)

# Display the image with rectangles around the recognized text regions
cv2.imshow('Text Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()