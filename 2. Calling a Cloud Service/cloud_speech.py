"""
This Python code takes a path input (i.e. Test.wav), calls the
google speech recognition API, and gets the result text.

Original Python code: 
https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

Edited by John Wu, 9/5/2018
"""

import numpy as np   
import speech_recognition as sr

def recognize(path):
    # use the audio file as the audio source
    # AUDIO_FILE = "D://hello.wav"
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        a = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return (a);
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ("Sorry, can't understand");
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ("Could not request results from service");


