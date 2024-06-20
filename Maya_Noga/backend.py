from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

from flask import Flask, request, jsonify

detected_objects = {}

model = MobileNetV2(weights = "imagenet")

def process_image(image):
    model.summary()
    img = Image.open('./static/images/' + image)

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
    return detected_objects

# app = Flask(__name__)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     byte_array = request.get_data()
#     print("start checking")
#     # Process the byte array as needed
#     # For example, save to a file
#     with open('uploaded_image.png', 'wb') as f:
#         f.write(byte_array)
#     return jsonify({'status': 'success', 'message': 'File uploaded successfully'})

# if __name__ == '_main_':
#     app.run(debug=True)