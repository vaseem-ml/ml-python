from django.shortcuts import render
import tensorflow as tf
from django.http import HttpResponse, JsonResponse
# Create your views here.
###loading libraries
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import os

#loading pickle
with open("sentiment/MFiles/normal/tokenizer.pickle", 'rb') as handle:
    tokenizer = pickle.load(handle)


checkpoint_dir = "sentiment/MFiles/normal/checkpoints/ckpt"
checkpoints = [checkpoint_dir + "/" + name for name in os.listdir(checkpoint_dir)]
latest_checkpoint = max(checkpoints, key=os.path.getctime)

model = load_model(latest_checkpoint)


def home(request):
    x_test = pad_sequences(tokenizer.texts_to_sequences([request.GET.get("sentiment")]), maxlen=300)
    score = model.predict([x_test])

    return HttpResponse(score[0][0])