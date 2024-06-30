import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained model
model = tf.keras.applications.ResNet50(weights='imagenet')

# Load and preprocess the image
img_path = "tinca.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)
decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions)

# Function to check if predicted label is a sea creature (consider using a more comprehensive marine creature list)
def is_sea_creature(label):
  seaCreatures=["tench","goldfish","great white shark","tiger shark","hammerhead shark","electric ray"," crampfish", "numbfish","stingray","sea snake","jellyfish","sea anemone","brain coral","sea slug", "nudibranch","chiton","Dungeness crab","rock crab"," Cancer irroratus","fiddler crab","king crab","American lobster","spiny lobster","crayfish","hermit crab","grey whale", "devilfish","killer whale", "grampus","sea wolf","dugong","sea lion","starfish","sea urchin","sea cucumber"]

  return label.lower() in seaCreatures
# Print the top predictions only if the predicted creature is a sea creature
for _, label, score in decoded_predictions[0]:
  if is_sea_creature(label):
    print(f"{label}")