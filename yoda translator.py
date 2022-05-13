import pyttsx3
import requests
engine = pyttsx3.init()
engine.setProperty('voice',0)
engine.setProperty('rate',0.9)
speech = input('Enter what to say in Yoda speak: ').replace(' ','%20')
request = requests.get('https://api.funtranslations.com/translate/yoda.json?text='+speech)
request = request.json()
engine.say(request['contents']['translated'])
engine.runAndWait()
