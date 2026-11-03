# Write a program to pronounce a list of names using the Win32 API.
# If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

import win32com.client
speaker=win32com.client.Dispatch("SAPI.Spvoice")
l = ["Rahul", "Nishant", "Harry"]
for name in l:
    speaker.Speak("ShoutOut to : "+name)
