import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
import os
from toolidentify import scan_tools

class HardwareGuruAssistant:
    def __init__(self, api_key):
        self.api_key = api_key
        self.classes = ['ESP32', 'Raspberry Pi', 'Raspberry Pi Pico', 'Led', 'Arduino']
        genai.configure(api_key=self.api_key)
        self.recognizer = sr.Recognizer()

    def is_gratitude_related(self, text):
        gratitude_keywords = [
            "thank", "grateful", "appreciate", "appreciation", "thanks",
            "gratitude", "thankful", "blessed", "gratified", "acknowledge"
        ]
        return any(keyword in text.lower() for keyword in gratitude_keywords)

    def listen_and_convert(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
        except sr.WaitTimeoutError:
            print("Timed out. No speech detected.")
            self.text_to_speech("Timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            self.text_to_speech("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Error connecting to Google Web Speech API: {e}")
            self.text_to_speech("its seems there is some error")

    def get_response(self, user_input):
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-exp-0827")
        response = model.generate_content(user_input)
        return response.text

    def text_to_speech(self, text):
        tts = gTTS(text, lang='en', tld='us')
        filename = 'temp.mp3'
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    def handle_input(self, input_text):
        if any(phrase in input_text.lower() for phrase in ["bye", "exit", "goodbye"]):
            print("Exiting the program. Goodbye!")
            return True

        if any(keyword in input_text.lower() for keyword in ["sparky","spark","hey","hello"]):
            print("Woke up! You can start speaking now.")
            self.text_to_speech("Hi there! Sparky at your service!")
            while True:
                # self.text_to_speech("Listening")
                input_text = self.listen_and_convert()
                if input_text:
                    if any(phrase in input_text.lower() for phrase in ["bye", "exit", "goodbye"]):
                        print("Exiting the program. Goodbye!")
                        self.text_to_speech("Goodbye!")
                        return True 
                    
                    if "detect items" in input_text.lower():
                        tools=scan_tools()
                        if len(tools) > 0:
                            labels= ",".join(tools)
                            input_text = f"summarize about {labels} in 50 words and tell a joke related to it"
                        else:
                            print("No tools detected")
                            self.text_to_speech("No known tools are detected")
                            input_text = ""
                    elif self.is_gratitude_related(input_text):
                        pass  # Keep input as is
                    else:
                        input_text = f"if '{input_text}' is related to hardware or electronics then summarize in 50 words else deny politely and don't add yes at the start of a sentence."
                    
                    if input_text:
                        response = self.get_response(input_text)
                        if response:
                            print(f"Response: {response}")
                            self.text_to_speech(response)
        return False  # No need to exit

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    assistant = HardwareGuruAssistant(API_KEY)
    
    while True:
        print("Listening... Say 'hey Sparky' to wake up:")
        assistant.text_to_speech("Say 'hey Sparky' to start")
        input_text = assistant.listen_and_convert()
        if input_text and assistant.handle_input(input_text):
            break  # Exit the main loop