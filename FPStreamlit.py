#Importing dependancies
import streamlit as st
from PIL import Image
import librosa
import numpy as np
import librosa.display
from pydub import AudioSegment
import matplotlib as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
from tensorflow import keras
from keras import layers
from keras.layers import (Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, 
                          Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D,
                          Dropout)
from keras.models import Model, load_model
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from keras.initializers import glorot_uniform
from keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import img_to_array, load_img


#Loading a file from user
st.write("Music Genre Recognition Application")
st.write("This is a Web App to predict genre of music")

file = st.sidebar.file_uploader("Please Upload an mp3 File Here", type=["mp3"])

#Labeling our genres
class_labels = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

#Loading our pre-trained model
model = load_model("/Users/frisbi01/Coding/DS course/Phase 3/Final Project/Genre Model/genre.h5")

#Making some functions for later use

def convert_mp3_to_wav(music_file):
    sound = AudioSegment.from_mp3(music_file)
    sound.export("music_file.wav", format="wav")

def extract_snippet(wav_file,t1,t2):
    wav = AudioSegment.from_wav(wav_file)
    wav = wav[1000*t1:1000*t2]
    wav.export("extracted.wav", format='wav')
    
def create_melspectrogram(wav_file):  
    y,sr = librosa.load(wav_file, duration=30)  
    mels = librosa.feature.melspectrogram(y=y,sr=sr) 
    mels_db = librosa.amplitude_to_db(mels, ref=np.max) 
    librosa.display.specshow(mels_db, sr = sr)  
    plt.savefig('melspectrogram.png')

#Labeling our genres  
class_labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    
def predict(image_data,model):

  image = image_data.resize((288,432))
  image = img_to_array(image_data)
  image = np.reshape(image,(1,288,432,4))
  prediction = model.predict(image/255)
  prediction = prediction.reshape((10,)) 
  class_label = np.argmax(prediction)
  return class_label,prediction


#Checking the user's input
if file is None:  
  st.text("Please upload an mp3 file")
else:  
  convert_mp3_to_wav(file)  
  extract_snippet("music_file.wav",120,150)   
  create_melspectrogram("extracted.wav")   
  
  image_data = load_img('melspectrogram.png',color_mode='rgba',target_size=(288,432))
  
  class_label,prediction = predict(image_data,model)   
  
  st.write("## The Genre of Song is "+class_labels[class_label])
  
  spec_or_prob = st.sidebar.radio("Select one of Below",("Probability Distribution","Mel Spectrogram"))

  prediction = prediction.reshape((10,)) 
  
  color_data = [1,2,3,4,5,6,7,8,9,10]
  my_cmap = cm.get_cmap('jet')
  my_norm = Normalize(vmin=0, vmax=10)

  if(spec_or_prob =="Probability Distribution"):
    fig,ax= plt.subplots(figsize=(6,4.5))
    ax.bar(x=class_labels,height=prediction,
    color=my_cmap(my_norm(color_data)))
    plt.xticks(rotation=45)
    ax.set_title("Probability Distribution Of The Given Song Over Different Genres")
  
    plt.show()
    st.pyplot(fig)

  if(spec_or_prob=="Mel Spectrogram"):
    st.image("melspectrogram.png")
    