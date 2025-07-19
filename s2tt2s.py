# speech_interface.py

import speech_recognition as sr
import pyttsx3


class SpeechInterface:
    def __init__(self, voice_id=None, rate=150, volume=1.0):
        # Initialize recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # TTS Config
        if voice_id is not None:
            self.tts_engine.setProperty('voice', voice_id)
        self.tts_engine.setProperty('rate', rate)
        self.tts_engine.setProperty('volume', volume)

    def listen(self, timeout=5, phrase_time_limit=10):
        """Captures speech input and converts to text."""
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                text = self.recognizer.recognize_google(audio)
                print("📝 You said:", text)
                return text
            except sr.UnknownValueError:
                print("⚠️ Could not understand audio.")
                return None
            except sr.RequestError:
                print("❌ Could not request results; check your internet connection.")
                return None
            except sr.WaitTimeoutError:
                print("⏱️ Listening timed out.")
                return None

    def speak(self, text):
        """Converts given text to speech."""
        if text:
            print("🔊 Speaking:", text)
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        else:
            print("⚠️ No text to speak.")

    def run_pipeline(self, response_text=None):
        """Optional: listen and speak in one go."""
        spoken_input = self.listen()
        if response_text:
            self.speak(response_text)
        return spoken_input


speech_io = SpeechInterface()

user_query = speech_io.listen()
speech_io.speak(user_query)
