
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()   
voice=engine.getProperty('voices')
#engine.setProperty('voice',voice[1].id) # voix  en ANglais
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()
    
def ecouter():
    try :
        with sr.Microphone() as source:
            print("Parler maintenant")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            
            # print(command)
            # engine.say(command)
            # engine.runAndWait()
        # else:
        #     print("desoler")
    except:
    
        pass
    return command


def lancer_assistant():
    command=ecouter()
    command=command.lower()
    print(command)
    # if 'bonjour' in command:
    #     text='bonjour, ca va?'
    #     parler(text)
        
    if 'mets la chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        # text='bonjour, ca va?'
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)
        
    elif 'heure' in command :
        
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)
        
    elif 'bonjour' in command:
        parler('Bonjour a toi comment tu vas?')
        
    else:
        
        print("je ne comprend pas")


    
lancer_assistant()
    
    