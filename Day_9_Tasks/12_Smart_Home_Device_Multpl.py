"""12. Smart Home Devices (Multiple Inheritance)
A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance."""

class WiFiDevice:
    def connect_wifi(self,network):
        print("Connecting to WiFi: ",network)

class VoiceAssistant:
    def voice_command(self,command):
        print("Executing voice command: ",command)

class SmartSpeaker(WiFiDevice,VoiceAssistant):
    def display_status(self,device_name):
        print("Device Name: ",device_name)
        print("Status: Active and Listening")

spk=SmartSpeaker()

spk.display_status("Jio Fiber")
spk.connect_wifi("SKL_Prsnl")
spk.voice_command("What is the Weather")
