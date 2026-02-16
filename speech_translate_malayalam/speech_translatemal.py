import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# initialize translator and TTS
translator = Translator()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak in English...")
    speak("Please speak in English")

    audio = recognizer.listen(source)

    try:
        # Speech to text (English)
        english_text = recognizer.recognize_google(audio, language="en-US")
        print("You said (English):", english_text)

        # Translate to Malayalam
        translated = translator.translate(english_text, src='en', dest='ml')
        malayalam_text = translated.text

        print("Malayalam Translation:", malayalam_text)
        speak("Translation completed")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        speak("Sorry, I could not understand")

    except sr.RequestError:
        print("Speech service error.")