import math
import easyocr
import cv2

img = cv2.imread('images/image3.jpg')
reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(img)
entity_obj = []
image_width, image_height, _ = img.shape
reference_point = (image_width / 2, image_height / 2)
distances = []

for detection in result:
    temp_dict = {}
    text = detection[1]
    bounding_box = detection[0]
    confidence  = detection[2]
    temp_dict.update({'text': text})
    temp_dict.update({'confidence': detection[2]})
    # Extract individual coordinates
    x_values = [point[0] for point in bounding_box]
    y_values = [point[1] for point in bounding_box]

    # Calculate top-left and bottom-right points
    top_left = (min(x_values), min(y_values))
    bottom_right = (max(x_values), max(y_values))

    # Calculate width and height of the bounding box
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    size = width * height
    temp_dict.update({'size': size})
    entity_obj.append(temp_dict)

    # Calculate the center point of the bounding box
    box_center = ((bounding_box[0][0] + bounding_box[2][0]) / 2, (bounding_box[0][1] + bounding_box[2][1]) / 2)
    # Calculate the distance between the center point and the reference point
    distance = math.sqrt((box_center[0] - reference_point[0]) ** 2 + (box_center[1] - reference_point[1]) ** 2)
    distances.append((text, distance))

sorted_words = sorted(distances, key=lambda x: x[1])
sorted_words.reverse()
line_no = 1
for s in sorted_words:
    for index, obj in enumerate(entity_obj):
        if obj['text'] == s[0]:
            entity_obj[index].update({'line_no': line_no})
            line_no = line_no + 1

largest_text_value = []
# largest_text = max(entity_obj, key=lambda x: (x['size'], x['confidence']))
# print(largest_text)
while True:
    temp_entity_object = entity_obj
    index, largest_text = max(enumerate(temp_entity_object), key=lambda x: (x[1]['size'], x[1]['confidence']))
    print("--> --> --> ", index, largest_text)
    if largest_text['confidence'] > 0.85:
        largest_text_value.append(largest_text)
        break
    else:
        temp_entity_object.remove(largest_text)

for obj in entity_obj:
    if obj['line_no'] == (largest_text_value[0]['line_no'] - 1):
        # if obj['size'] > largest_text_value[0]['size'] - 2000 and obj['size'] < largest_text_value[0]['size'] + 2000:
        if obj['confidence'] > 0.85:
            largest_text_value.append(obj)
    elif obj['line_no'] == (largest_text_value[0]['line_no'] + 1):
        # if obj['size'] > largest_text_value[0]['size'] - 2000 and obj['size'] < largest_text_value[0]['size'] + 2000:
        if obj['confidence'] > 0.85:
            largest_text_value.append(obj)

floating_values = []
for obj in entity_obj:
    if '.' in obj['text'] and obj['confidence'] > 0.85:
        floating_values.append(obj)
    elif 'MRP' in obj['text'] and obj['confidence'] > 0.85:
        floating_values.append(obj)

print("floating values : ", floating_values)
print("=======================================================")
print("-->  Text with largest font size:", largest_text_value)
print("Result : ", result)

