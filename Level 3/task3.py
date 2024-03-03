#level 3 task 3 a simple notes taking automation application that records audio from the microphone 
#and saves it to a text file
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import os

def speak(text):
    """Speaks provided text"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Records audio from the microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You said: " + said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def create_note(text):
    """Creates a text file as a note"""
    date = datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    # Create a 'notes' folder if it doesn't exist
    notes_dir = "notes"
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    file_path = os.path.join(notes_dir, file_name)
    with open(file_path, "w") as f:
        f.write(text)
    speak("Note saved successfully.")

def main():
    speak("Ready to take notes. Say 'start' to begin.")

    while True:
        command = get_audio()

        if command == 'start':
            notes = ""
            speak("Start speaking your notes.")
            while True:
                note_line = get_audio()
                if note_line == 'save':
                    create_note(notes)
                    break  # Exit the inner loop
                else:
                    notes += note_line + " "  
        elif command == 'quit':
            speak("Exiting the note-taking application. Goodbye!")
            break
        else:
            speak("Unrecognized command.")

if __name__ == "__main__":
    main()
