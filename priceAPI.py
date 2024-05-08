import re
import easyocr
import numpy as np
from PIL import Image
import matplotlib.image as mpimg
from flask import Flask, request

application = app = Flask(__name__)


@app.route("/extractprice", methods=['POST'])
def textextract():
    print("Function Running")
    image_file = request.files.get('image')

    img = Image.open(image_file)
    img_array = np.array(img)
    print(img)
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=True)

    result = reader.readtext(img_array)
    price = ''
    integers = []

    for list in result:
        print("value : ",list[1] + " confidence : ",list[2])
        prices1 = re.findall(r'\b\d+\.\d{1,2}\b(?!\d)', list[1])
        prices2 = re.findall(r'\b\d+\.\d{1,2}\b(?!\.\d)', list[1])
        if prices1 == prices2 and len(prices1) != 0 and float(prices1[0]) >= 10.00:
            price = prices1
            break
        else:
            integers.append(re.findall(r'(?<!\d\.)\b\d{2}\b(?!\.\d)', list[1]))

    IntPriceList = [item for sublist in integers for item in sublist]

    if len(price) != 0:
        value = float(price[0])
        return {"price": int(value)}
    else:
        try:
            return {"price": int(IntPriceList[0])}
        except:
            return {"price": 0}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
