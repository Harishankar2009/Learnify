import speech_recognition as sr
import logging
from config import load_config

class SpeechRecognizer:
    def __init__(self, config):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = config['speech_recognition']['language']
        self.timeout = config['speech_recognition']['timeout']
        self.phrase_time_limit = config['speech_recognition']['phrase_time_limit']
        self.logger = logging.getLogger(__name__)

    def recognize_speech(self):
        with self.microphone as source:
            self.logger.info("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)
                text = self.recognizer.recognize_google(audio, language=self.language)
                self.logger.info(f"Recognized speech: {text}")
                return text
            except sr.UnknownValueError:
                self.logger.error("Google Speech Recognition could not understand the audio.")
                return None
            except sr.RequestError as e:
                self.logger.error(f"Could not request results from Google Speech Recognition service; {e}")
                return None

if __name__ == "__main__":
    config = load_config()
    recognizer = SpeechRecognizer(config)
    print(recognizer.recognize_speech())
    print("Listening...")