import os
user = input("Enter your name here:")
speak = f"Welcome {user} to the quiz."
command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
os.system(command)
question={
    "what is the capital of India?":"DELHI",
    "What is the national bird of India?":"PEACOCK",
    "Which City is known as the city of joy?":"KOLKATA",
}


if __name__ == '__main__':
    speak=question.keys()
    i=0
    n=0
    for ques in question:
        n+=1
        print(ques)
        command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{ques}\')"'
        os.system(command)
        ans=input("Enter Your Answer:")

        # print(ans.upper())
        if ans.upper() == question[ques]:
            speak="You are right"
            command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
            os.system(command)
            i+=1
        else:
            speak="You are wrong"
            command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
            os.system(command)


    if i==n:
        print(f"Congratulations!! your score is {i} out of {n}")
        speak=f"Congratulations!! At the end of the game your score is {i} out of {n} and it is the highest score."
        command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
        os.system(command)
    else:
        print(f"At the end of the game your score is {i} out of {n}")
        speak=f"At the end of the game your score is {i} out of {n}"
        command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{speak}\')"'
        os.system(command)



bye=f"bye bye {user}"
command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{bye}\')"'
os.system(command)