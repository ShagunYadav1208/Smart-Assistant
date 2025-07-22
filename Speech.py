import speech_recognition as sr
import pyttsx3

def correct_pronunciation(word):
    engine = pyttsx3.init()
    engine.say("The correct pronunciation is {}".format(word))  # For simplicity, assuming input word is already correct
    engine.runAndWait()

def take_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Speak something.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Use Google Web Speech API to recognize the audio
        print("You said: " + text)
        correct_pronunciation(text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    take_voice_input()