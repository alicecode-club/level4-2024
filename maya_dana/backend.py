from flask import Flask, request, render_template
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np
from io import BytesIO
import os
import requests

app = Flask(__name__)
model = MobileNetV2(weights='imagenet')

def image(img):
    resized_img = img.resize((224, 224))
    img_array = np.array(resized_img)
    input_array = np.expand_dims(img_array, axis=0)
    input_data = preprocess_input(input_array)
    return input_data


def predict_breed(img):
    input_data = image(img)
    predictions = model.predict(input_data)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    result = decoded_predictions[0][1]
    return result


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/new_dog', methods=['POST'])
def new_dog():
    response = requests.get("https://api.thedogapi.com/v1/images/search").json()[0]["url"]
    img_response = requests.get(response)
    img = Image.open(BytesIO(img_response.content))
    breed = predict_breed(img)
    return render_template('index.html', dog_image=response, breed=breed)


@app.route('/upload', methods=['POST'])
def upload_picture():
    if 'file' not in request.files:
        return 'No file found', 400
    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400
    
    if not os.path.exists('./static/images'):
        os.makedirs('./static/images')

    file_path = os.path.join('./static/images', file.filename)
    file.save(file_path)

    img = Image.open(file_path)
    breed = predict_breed(img)

    return render_template('index.html', picture_path=file_path, breed=breed)


if __name__ == '__main__':
    app.run()