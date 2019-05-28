import speech_recognition as sr
import RPi.GPIO as GPIO
r = sr.Recognizer()

audio = 'voice.wav'
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
with sr.AudioFile(audio) as source:
        print("say something")
        audio = r.record(source)
        print("done")
try:
        text = r.recognize_google(audio)
        print("you said",text)
except Exception as e:
        print(e)

if text == "on":
	GPIO.output(18,GPIO.HIGH)
	print ("lights on")
elif text == "off":
	GPIO.output(18,GPIO.LOW)
	print ("lights off")
else:
	print("invalid")
