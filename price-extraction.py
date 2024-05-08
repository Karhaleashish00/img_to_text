import easyocr
import cv2
from spellchecker import SpellChecker
import re

def textextract(enhancedimg):
    # Read the enhanced image
    img = cv2.imread(str(enhancedimg))

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=True)

    # Perform OCR on the enhanced image
    result = reader.readtext(img)
    string_result = ''
    price = ''
    integers = []

    # Initialize spell checker
    spell = SpellChecker()

    # Define a regular expression pattern to match numbers
    number_pattern = r'\b\d+(\.\d+)?\b'

    # # Iterate through each tuple in the result list
    # for item in result:
    #     try:
    #         # Extract the word from the tuple (which is at index 1)
    #         word = item[1]
    #
    #         # Perform spell checking on the word
    #         corrected_word = spell.correction(word)
    #
    #         # Extract and correct numbers from the word using regular expressions
    #         try:
    #             numbers = re.findall(number_pattern, corrected_word)
    #         except:
    #             pass
    #
    #         for num in numbers:
    #             # Perform spell checking on the number
    #             corrected_num = spell.correction(num)
    #             # Replace the original number with the corrected one in the word
    #             corrected_word = corrected_word.replace(num, corrected_num)
    #
    #         # Append the corrected word to the result string
    #         string_result += corrected_word + ' '
    #     except:
    #         pass

    for list in result:
        prices1 = re.findall(r'\b\d+\.\d{2}\b(?!\d)', list[1])
        prices2 = re.findall(r'\b\d+\.\d{2}\b(?!\.\d)', list[1])
        if prices1 == prices2 and len(prices1) != 0 and float(prices1[0])>= 10.00:
            price = prices1
            break
        else:
            integers.append(re.findall(r'(?<!\d\.)\b\d{2}\b(?!\.\d)', list[1]))
    # Return the corrected result
    print("price : ", price)
    flattened_list = [item for sublist in integers for item in sublist]
    # print(flattened_list)
    # print("integers : ",flattened_list)
    if len(price) == 0:
        print("price : ", flattened_list[0])


    return string_result

# Example usage:
textextract('images/image3.jpg')
