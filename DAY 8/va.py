# pip install pyttsx3 SpeechRecognition
import speech_recognition as sr
import pyttsx3


# Initialize the text-to-speech engine
engine = None
try:
    engine = pyttsx3.init()
except Exception as e:
    print("⚠️ pyttsx3 initialization failed:", e)

# Function to make the assistant speak
def speak(text):
    if engine is None:
        print(text)
        return

    try:
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("⚠️ Text-to-speech error:", e)
        print(text)

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
    except sr.WaitTimeoutError:
        print("⚠️ No speech detected within the timeout period.")
        speak("I did not hear anything. Please try again.")
        return ""
    except OSError as e:
        print("⚠️ Microphone error:", e)
        speak("I cannot access the microphone. Please check your audio device.")
        return ""
    except Exception as e:
        print("⚠️ Audio capture error:", e)
        speak("I could not capture audio right now.")
        return ""

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print("🗣️ You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't understand.")
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("❌ Speech service error:", e)
        speak("Sorry, my speech service is down.")
        return ""
    except Exception as e:
        print("⚠️ Recognition error:", e)
        speak("Something went wrong while understanding you.")
        return ""

if __name__ == '__main__':
    speak("Hello! I'm your virtual assistant. How can I help you?")

    try:
        while True:
            command = listen()
            if not command:
                continue

            if "hi" in command:
                speak("Hello, how is your day?")
            elif "python" in command:
                speak("Python classes will end today")
            elif 'your name' in command:
                speak("I am your Python assistant!")
            elif 'pfs50' in command:
                speak('11 members are present today')
            elif 'stop' in command or 'exit' in command or 'bye' in command:
                speak("Okay bye bye! Have a good day")
                break
            else:
                speak("Sorry, I can't do that yet.")
    except KeyboardInterrupt:
        speak("Goodbye! Have a great day.")
