from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

detected_objects = []
duplicate = 0

model = MobileNetV2(weights = "imagenet")
model.summary()

img = Image.open("test_images/chain.jpg")

resized_img = img.resize((224, 224))
img_array = np.array(resized_img)

input_array = np.expand_dims(img_array,axis=0)

input_data = preprocess_input(input_array)

predictions = model.predict(input_data)

decoded_predictions = decode_predictions(predictions, top=1)
top_prediction = decoded_predictions[0][0][1]

detected_objects.append(top_prediction.replace('_', ' ').title())
print(detected_objects[0])

if top_prediction in detected_objects:
    duplicate += 1