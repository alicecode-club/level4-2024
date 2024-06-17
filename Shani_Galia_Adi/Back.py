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
  seaCreatures=["tench, Tinca tinca","goldfish, Carassius auratus","great white shark, white shark, man-eater, man-eating shark, Carcharodon caharias","tiger shark, Galeocerdo cuvieri","hammerhead, hammerhead shark","electric ray, crampfish, numbfish, torpedo","stingray","sea snake","jellyfish","sea anemone, anemone","brain coral","sea slug, nudibranch","chiton, coat-of-mail shell, sea cradle, polyplacophore","chambered nautilus, pearly nautilus, nautilus","Dungeness crab, Cancer magister","rock crab, Cancer irroratus","fiddler crab","king crab, Alaska crab, Alaskan king crab, Alaska king crab, Paralithodesamtschatica","American lobster, Northern lobster, Maine lobster, Homarus americanus","spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish","crayfish, crawfish, crawdad, crawdaddy","hermit crab","grey whale, gray whale, devilfish, Eschrichtius gibbosus, Eschrichtius rostus","killer whale, killer, orca, grampus, sea wolf, Orcinus orca","dugong, Dugong dugon","sea lion","starfish, sea star","sea urchin","sea cucumber, holothurian"]

  return label.lower() in seaCreatures
# Print the top predictions only if the predicted creature is a sea creature
for _, label, score in decoded_predictions[0]:
  if is_sea_creature(label):
    print(f"{label}: {score:.2f}")