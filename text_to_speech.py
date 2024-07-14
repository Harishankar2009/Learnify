import pyttsx3
import logging
from config import load_config

class TextToSpeech:
    def __init__(self, config):
        self.engine = pyttsx3.init()
        self.language = config['text_to_speech']['language']
        self.rate = config['text_to_speech']['rate']
        self.volume = config['text_to_speech']['volume']
        self.logger = logging.getLogger(__name__)

        # Set properties
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
        self.engine.setProperty('voice', self.language)

    def speak(self, text):
        self.logger.info(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    config = load_config()
    tts = TextToSpeech(config)
    tts.speak("Hello, how can I assist you today?")
