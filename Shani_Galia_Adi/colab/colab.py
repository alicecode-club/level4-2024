from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

model = MobileNetV2(weights='imagenet')

model.summary()

img = Image.open("panda.jpg")

resized_img = img.resize( (224, 224))
img_array =np.array(resized_img)
img_array

input_array = np.expand_dims(img_array,axis=0)
input_array.shape

input_data = preprocess_input(input_array)
input_data

predictions = predictions = model.predict(input_array)
predictions.shape
least_likely_index = np.argmin(predictions[0])
print(f"Least likely class (index): {least_likely_index}")

top_3_predictions = decode_predictions(predictions, top=3)[0]
for prediction in top_3_predictions:
    class_id, class_name, probability = prediction
    print(f"Class: {class_name}, Probability: {probability:.2f}")