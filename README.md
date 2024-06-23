# Thomas: A Virtual Assistant

Thomas is a virtual assistant designed to respond to voice commands, similar to popular assistants like Alexa or Google Assistant. The project uses various libraries including `speech_recognition` for recognizing speech, `gtts` for text-to-speech, and `openai` for processing commands using GPT-3.5.

## Features

- **Speech Recognition**: Uses the `speech_recognition` library to convert spoken words into text.
- **Text-to-Speech**: Uses the `gtts` library to convert text responses into spoken words.
- **Natural Language Processing**: Integrates OpenAI's GPT-3.5 to process and respond to user commands.
- **Voice Activation**: Listens for the wake word "Thomas" to activate.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your computer.
- Pip package installer.
- Google API credentials for speech recognition.
- OpenAI API key.
- Required Python libraries:
  - `speech_recognition`
  - `webbrowser`
  - `gtts`
  - `pygame`
  - `openai`

## Installation

1. Clone the repository or download the script.

2. Install the required Python libraries using pip:
    ```sh
    pip install speechrecognition gtts pygame openai
    ```

3. Ensure you have a working microphone connected to your computer.

4. Obtain an OpenAI API key from the OpenAI website and replace `YOUR_API_KEY` in the script with your actual API key.

## Usage

1. Run the script:
    ```sh
    python thomas.py
    ```

2. The assistant will prompt you to say "Thomas" to activate it.

3. After activation, give your command. The assistant will process your command and respond accordingly.

## Script Breakdown

### Initialization

The script initializes the speech recognizer and defines the `speak` function to convert text to speech.

```python
recognizer = sr.Recognizer()

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
```

### Command Processing

Defines the `aiProcess` function to interact with the OpenAI API and process commands.

```python
def aiProcess(command):
    client = OpenAI(api_key="YOUR_API_KEY")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Thomas skilled in general tasks like Alexa. Give short responses"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content
```

### Main Loop

Listens for the wake word "Thomas" and processes subsequent commands.

```python
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
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## Acknowledgements

- Inspired by popular virtual assistants like Alexa and Google Assistant.
- Uses OpenAI's GPT-3.5 for natural language processing.
- Speech recognition powered by Google Speech Recognition.

## Contact

If you want to contact me, you can reach me at `keshavdaga81@gmail.com`.
