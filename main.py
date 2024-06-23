import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
from openai import OpenAI
import pygame

recognizer = sr.Recognizer() #Speech Recognition


def speak(text):
    tts = gTTS(text, lang='en')
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
    api_key="YOUR_API_KEY",
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Thomas skilled in general tasks like Alexa. Give short responses"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    output = aiProcess(c)
    speak(output)

if __name__ == "__main__":
    speak("Say Thomas to activate")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower() == 'thomas'):
                speak("Addrrrreeeeee")
                with sr.Microphone() as source:
                    print("Thomas Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
            else:
                speak("No Good. Try Again")

        except Exception as e:
            print(e)