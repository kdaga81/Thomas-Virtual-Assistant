import speech_recognition as sr
from gtts import gTTS
import os
from openai import OpenAI
import pygame

# Initialize Speech Recognition
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech and play it."""
    # Generate speech audio file
    tts = gTTS(text, lang='en')
    tts.save("temp.mp3")
    
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Wait for speech to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up: unload audio and remove temporary file
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    """Process user command using OpenAI GPT-3 and return AI response."""
    client = OpenAI(
        api_key="YOUR_API_KEY",  # Replace with your OpenAI API key
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
    """Process the command and speak the AI response."""
    output = aiProcess(c)
    speak(output)

if __name__ == "__main__":
    # Initial prompt to activate the assistant
    speak("Say Thomas to activate")
    
    while True:
        # Initialize Speech Recognition for listening
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                # Listen for a command within the specified timeout
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                
            # Use Google Speech Recognition to convert audio to text
            command = r.recognize_google(audio)
            
            # Check if the user said "thomas" to activate the assistant
            if command.lower() == 'thomas':
                speak("Addrrrreeeeee")
                
                # Listen again for the user's actual command
                with sr.Microphone() as source:
                    print("Thomas Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    # Process and respond to the user's command
                    processCommand(command)
            else:
                speak("No Good. Try Again")

        except Exception as e:
            print(e)
