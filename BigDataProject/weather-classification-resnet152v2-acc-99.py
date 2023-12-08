
import keras
import numpy as np
import pandas as pd
from glob import glob
from tqdm import tqdm
import os
import gdown

# Data
from tensorflow.image import resize
from sklearn.model_selection import StratifiedShuffleSplit
from tensorflow.keras.utils import load_img, img_to_array
# Data Viz
import seaborn as sns
import matplotlib.pyplot as plt

# TL Model
from tensorflow.keras.applications import ResNet50, ResNet50V2, InceptionV3, Xception, ResNet152, ResNet152V2

# Model
from keras import Sequential
from keras.layers import Dense, GlobalAvgPool2D, Dropout
from keras.models import load_model

# Callbacks 
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Model Performance
from sklearn.metrics import classification_report

# Model Viz
from tensorflow.keras.utils import plot_model




def load_image(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.JPEG','.jpeg')):  # Add more file extensions if needed
            img_path = os.path.join(folder_path, filename)
            img = resize(img_to_array(load_img(img_path))/255., (256, 256))
            images.append(img)
    return images

def download_and_load_model(url_id, output_id):
    # Demander à l'utilisateur s'il veut télécharger automatiquement le modèle
    user_input = input("do you want the script to automatically download the model.h5 ?  (yes/no): ").lower()

    if user_input == "yes" or user_input == "y":
        # Télécharger le fichier depuis Google Drive
        gdown.download(id=url_id, output=output_id, quiet=False)

        # Vérifier si le fichier a été téléchargé avec succès
        if os.path.exists(output_id):
            # Charger le modèle avec Keras
            model_v3 = load_model(output_id)
            print("Model load with success.")
        else:
            print("error during the download")
    else:
        print("No download, please put the path to link your folder model to the folder model in Docker")

url_id = "1hzfqu8t3T50nZ0h2WN3ayYZJ335_xGcH"
output_id = "./model/ResNet152V2-Weather-Classification-03.h5"

download_and_load_model(url_id, output_id)
model_v3 = load_model('./model/ResNet152V2-Weather-Classification-03.h5')


images = load_image("./input")

class_names = ['cloudy','foggy','rainy','shine','sunrise']

liste_image=[]
liste_pred=[]
for i in range(len(images)):
    
    # Get image
    image = images[i]
    
    # Make Prediction
    pred = class_names[np.argmax(model_v3.predict(image[np.newaxis,...]))]
   
    liste_image.append(f"image{i}")
    liste_pred.append(pred)

df = pd.DataFrame(list(zip(liste_image,liste_pred)), columns=["image", "prediction"])

print(os.getcwd())

df.to_csv("./output/prediction.csv") 




