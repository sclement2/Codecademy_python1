class Speaker:
    brand = "Beatpill" # class variable

    def __init__(self, color, model):
        self._color = color # private instance attribute
        self._model = model # private instance attribute

    def power_on(self):
        print(f"Powering on {self._color} {self._model} speaker.")    

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker.")

speaker_one = Speaker("black", "85XB5")
speaker_two = Speaker("red", "Y8F33")

speaker_one.power_on()
speaker_two.power_off()

class SmartSpeaker(Speaker):
    def __init__(self, color, model, voice_assistant):
        super().__init__(color, model)
        self._voice_assistant = voice_assistant

    def say_hello(self):
        print(f"Hello, I am {self._voice_assistant}")


smart_speaker_one = SmartSpeaker("black", "XYZ123", "Alexa")

smart_speaker_one.power_on()
smart_speaker_one.say_hello()