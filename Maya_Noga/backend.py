from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

detected_objects = {"Chain":0}

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
top_prediction = top_prediction.replace('_', ' ').title()

detected_objects[top_prediction.replace('_', ' ').title()]=0
if top_prediction in detected_objects:
    updated = detected_objects[top_prediction] = detected_objects.get(top_prediction, 0) + 1
print(detected_objects)
