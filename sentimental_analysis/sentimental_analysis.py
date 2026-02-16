import speech_recognition as sr
from textblob import TextBlob
import pyttsx3

# text to speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# speech recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak now...")
    speak("Speak now")
    
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # sentiment analysis
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😔"
        else:
            sentiment = "Neutral 😐"

        print("Sentiment:", sentiment)
        speak(f"Your sentiment is {sentiment}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand")
    except sr.RequestError:
        print("Speech service error.")
        