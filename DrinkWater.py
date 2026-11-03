import os
import time

Repeat_Interval=10
while True:
    command=(
        'PowerShell -Command "Add-Type -AssemblyName System.Speech; '
        '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        '$speak.Speak(\'Hey Zoya, drink water!\')"'
    )
    os.system(command)
    time.sleep(Repeat_Interval)
