from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

model = MobileNetV2(weights = "imagenet")
model.summary()
img = Image.open("goldfish.jpg")
resized_img = img.resize((224, 224))
img_array = np.array(resized_img)
img_array
img_array.shape
input_array = np.expand_dims(img_array,axis=0)
input_array.shape
input_data = preprocess_input(input_array)
input_data
predictions = model.predict(input_data)
predictions
print(np.argmin(predictions, axis=1))
for name, desc, score in decode_predictions(predictions, top=3)[0]:
  print("{} - probability of ({:.2f}%)".format(desc.replace("_"," ").capitalize(), score*100))