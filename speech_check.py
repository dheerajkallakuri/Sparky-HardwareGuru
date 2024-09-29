import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
import os


API_KEY = "YOUR_API_KEY"

def listen_and_convert():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Say something:")
            audio = recognizer.listen(source, timeout=5)  # Adjust the timeout as needed

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
    except sr.WaitTimeoutError:
        print("Timed out. No speech detected.")
        return None
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Web Speech API: {e}")
        return None

def get_response(user_input):
        # Generate a response using OpenAI's API
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-exp-0827")
        response = model.generate_content(user_input)
        return response.text

if __name__ == "__main__":
    while True:
        input_text = listen_and_convert()
        if input_text:
            print(f"Converted text: {input_text}")
            # response = get_response(input_text)
            response = input_text
            if response:
                print(response)
                acc = 'us'
                tts = gTTS(text=response, lang='en', tld=acc)
                filename = 'temp.mp3'
                tts.save(filename)

                playsound(filename)

                os.remove(filename)
