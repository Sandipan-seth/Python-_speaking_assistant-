import os
import time
user=input("Enter your name:")
timeStamp= time.strftime("%H:%M:%S")
# print(timeStamp)
x=timeStamp
speak = f"Welcome {user} to this speaking bot.The time is {x}."
if __name__ == '__main__':
    command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
    os.system(command)
bye=f"bye bye {user}"
while True:
    if __name__ == '__main__':
        y=input("Enter the command:")
        if y=='q':
            speach = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{bye}\')"'
            os.system(speach)
            break
        speach = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{y}\')"'
        os.system(speach)
