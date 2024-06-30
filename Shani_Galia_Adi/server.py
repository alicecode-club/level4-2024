from flask import Flask, request, render_template, send_from_directory
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('static', 'opening.html')

model = tf.keras.applications.ResNet50(weights='imagenet')

# Function to check if predicted label is a sea creature
def is_sea_creature(label):
    sea_creatures = ["tench", "goldfish", "great white shark", "tiger shark",
                     "hammerhead shark", "electric ray", "crampfish", "numbfish",
                     "stingray", "sea snake", "jellyfish", "sea anemone", "brain coral",
                     "sea slug", "nudibranch", "chiton", "Dungeness crab", "rock crab",
                     "Cancer irroratus", "fiddler crab", "king crab", "American lobster",
                     "spiny lobster", "crayfish", "hermit crab", "grey whale", "devilfish",
                     "killer whale", "grampus", "sea wolf", "dugong", "sea lion", "starfish",
                     "sea urchin", "sea cucumber"]
    return label.lower() in sea_creatures

@app.route('/upload', methods=['POST'])
def upload_picture():
    # Validate and save the uploaded file
    if 'file' not in request.files:
        return 'No file found', 400
    

    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400

    if not os.path.exists('./static/images'):
        os.makedirs('./static/images')

    # Use secure_filename to prevent security vulnerabilities
    filename = secure_filename(file.filename)
    file.save(os.path.join('./static/images/', filename))

    # Preprocess the uploaded image
    img_path = os.path.join('./static/images/', filename)
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions)

    # Process and display results
    results = []
    for _, label, score in decoded_predictions[0]:
        if is_sea_creature(label):
            results.append(f"{label} ({score:.2f})")

    return render_template('picture.html', picture_path=os.path.join('./static/images/', filename), information=results)


def do_stuff_with_picture(filename):
    results = "Basic information about the image, cool AI stuff"
    return results

if __name__ == '__main__':
    app.run()