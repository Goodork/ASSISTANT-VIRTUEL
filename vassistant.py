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

#engine.setProperty("rate", 170)


# Deuxieme partie creation de fonction talk.

def talk(text): # Capacite de lecture d'un text
    engine.say(text)
    engine.runAndWait()
    
# 3eme partie : Creation great me : Salutation

def greetme():
    current_hour= int(datetime.datetime.now().hour) # recuperer l'heure actuelle.
    if 0<= current_hour <=12 :
        talk(" Bonjour honorable excelence gyl neuman")
    if 1<= current_hour <= 18:
        talk(" Bon apres midi  honorable excelence gyl neuman")    
        
    if current_hour>=18 and current_hour!=0 :
        talk(" Bonsoir honorable excelence gyl neuman")
 # set french femel voice
voices = engine.getProperty("voices") # recuperer les langues presente sur le systeme d'exploitation.

engine.setProperty("voice",voices[0].id)
greetme()
engine.say("comment vas tu?")
engine.runAndWait()

# 4 eme partie : creation de la fonction alexa command

def alexa_command():
    with sr.Microphone()  as source:
        print("listening....")
        
        #listener.pause_threshold=5  definir une pause pour permettre a alexa d'ecouter.
        voice=listener.listen(source)
        
        command= listener.recognize_google(voice, language="fr-FR")
        command= command.lower()
        print(command)
        
        if "alexa" in command:
            command=command.replace("alexa","")
            print(command)
    return command
            
    # 6eme partie : Creation de la fonction  run_alexa
def run_alexa():
    command=alexa_command()
    if "musique" in command :
        
        song=command.replace("musique", "")
        talk("musique en cours ...")
        
        pywhatkit.playonyt(song)
        
    elif "heure" in command:
        time=datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("il est actuellement: " + time)
        
        
    elif "qui est" in command:
        person=command.replace("qui est", "")
        wikipedia.set_lang("fr") # faire la recherche sur wikipedia en francais.
        info= wikipedia.summary(person, 1)
        
        
    elif "sortir" in command:
        talk("Desole, je suis un peu souffrante en ce moment. ")
        
        
    elif "en couple" in command:
        talk("non pas encore, mon coeur est encore a conquerir ")
        
    elif "blague" in command:
        
        jokes=[""] # voir apres pour terminer la blague
        
    elif " et toi" in command:
        msgs=["Je fais juste un truc","je vais bien !","Bien","je suis bien et toi "]
        talk(random.choice(msgs))
        
        
    elif "desactive toi" in command:
        talk("merci de m'avoir utilisé , gyl neuman")
        sys.exit()
        
    else:
        
        talk("pourrait tu repeter , je n'ai pas bien compris")
        
 
 
 
run_alexa()      
# while True:
#     run_alexa()
        