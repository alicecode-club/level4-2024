from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

model = MobileNetV2(weights = "imagenet")
model.summary()
img = Image.open("shih-tzu.jpg")
resized_img = img.resize((224, 224))
img_array = np.array(resized_img)

input_array = np.expand_dims((img_array), axis=0)
input_array.shape
input_data = preprocess_input(input_array)

predictions = model.predict(input_data)
predictions.shape

for name, desc, score in decode_predictions(predictions, top=1)[0]:
  print(f"{desc}")
