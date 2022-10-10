""" Transcrire une voix en texte . """


"""
import sys
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

# Initialisation 1er partie
listener=sr.Recognizer()
engine=pyttsx3.init()

engine.setProperty("voice","french")

def transcription():
    with sr.Microphone()  as source:
        print("listening....")
        
        #listener.pause_threshold=5  definir une pause pour permettre a alexa d'ecouter.
        voice=listener.listen(source)
        
        command= listener.recognize_google(voice, language="fr-FR")
        command= command.lower()
        print(command)
        
    return command

transcription()

"""

import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print("Speak :")
    
    audio= r.listen(source)
    
    
    try:
        
        text=r.recognize_google(audio)
        print("you said this : {} ".format(text))

    except:
        
        print("Sorry could not recognize your voice try again")
        

