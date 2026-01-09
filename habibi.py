import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import wikipedia
import pyjokes

# Initialize the recognizer and engine
listener = sr.Recognizer()
habibi = pyttsx3.init()

def talk(text):
    habibi.say(text)
    habibi.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source) # Helps with background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'habibi' in command:
                command = command.replace('habibi', '')
                return command.strip()
            else:
                # If name isn't called, ignore or ask to repeat
                return "word_missing"
    except Exception as e:
        print(e)
        return ""
    return ""

def run_habibi():
    command = take_command()
    print(f"User Said: {command}") # Debugging print

    if command == "word_missing":
        talk("Yes? I am listening.") # Better than the long error message
        return
    
    if command == "":
        return

    # --- LOGIC ---
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
        
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'open facebook' in command:
        talk("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        
    elif 'open youtube' in command:
        talk("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
        
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        try:
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)
        except:
            talk("I could not find anything on Wikipedia about that.")
            
    elif 'yourself' in command:
        a = "I am Habibi, your virtual assistant. Developed by the team Quantum Developers."
        print(a)
        talk(a)
        
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        talk('Hahahaha')

    elif "dubai" in command:
        talk("Not Dubai, I am Habibi from Bangladesh")
        
    elif "poem" in command:
        talk("In a gentle glow, Mysteries dance and secrets flow.")
        talk("Ami tomaka bhalobashi") # "I love you" in Bengali
        
    elif 'stop' in command or 'exit' in command:
        talk("Goodbye!")
        exit() # Kills the program

    else:
        talk("I did not get that, but I will search for it.")
        pywhatkit.search(command)

# --- MAIN LOOP ---
# This makes it run forever until you say "Stop"
if __name__ == "__main__":
    while True:
        run_habibi()
