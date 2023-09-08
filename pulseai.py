import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listner = aa.Recognizer()
machine = pyttsx3.init()
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)
machine.setProperty('rate', 1.5 * 100)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listner.listen(origin)
            instruction = listner.recognize_google(speech)
            instruction = instruction.lower()
            if "pulse" in instruction:
                instruction = instruction.replace('Pulse', ' ')
                print(instruction)
                return instruction
    except:
        return None

def play_Pulse():
    instruction = input_instruction()
    
    if instruction is not None:  
        
        if "play" in instruction:
            song = instruction.replace('pulse play', '')
            print("playing " + song)
            talk("playing " + song)
            pywhatkit.playonyt(song)
            play_Pulse()
        
        elif "time" in instruction:
            time = datetime.datetime.now().strftime('%I:%M:%p')
            print('current time ' + time)
            talk('current time ' + time)
            play_Pulse()
        
        elif "date" in instruction:
            date = datetime.datetime.now().strftime('%d /%m /%Y')
            print("Today's date " + date)
            talk("Today's date " + date)
            play_Pulse()
        
        elif "how are you" in instruction:
            print("I am fine, What about you ? ")
            talk("I am fine, What about you?")
            play_Pulse()
        
        elif "what is your name" in instruction:
            print("My name is Pulse AI, you can call me Pulse.")
            talk("My name is Pulse AI, you can call me Pulse.")
            play_Pulse()
        
        elif "who is" in instruction:
            human = instruction.replace('who is', '').strip()
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
            play_Pulse()

        elif "objective" in instruction:
            print("To present ourself in the interview for GDSC")
            talk("To present ourself in the interview for G D S C")
            play_Pulse()
        
        elif "who created you" in instruction:
            print("Yash Thakur from T E, artificial intelligence and Data science department, created me.")
            talk("Yash Thakur from T E, artificial intelligence and Data science department, created me")
            play_Pulse()

        elif "ganpati bappa" in instruction:
            print("Morya")
            talk("morya")

            play_Pulse()

        

        else:
            talk("Sorry, I don't know that.")

play_Pulse()
