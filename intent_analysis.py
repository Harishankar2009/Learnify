import logging 

class IntentAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def analyze_intent(self, command):
        self.logger.info(f"Analyzing intent for command: {command}")
        if 'hello' in command or 'hi' in command:
            return 'greetings'
        elif 'bye' in command or 'goodbye' in command:
            return 'farewell'
        elif 'essay' in command:
            return 'generate_essay'
        elif 'lesson' in command:
            return 'start_lesson'
        else:
            return 'Unknown'
if __name__  == '__main__':
    analyzer = IntentAnalyzer()
    print(analyzer.analyze_intent('hello'))
    print(analyzer.analyze_intent('bye'))
    print(analyzer.analyze_intent('write an essay'))
    