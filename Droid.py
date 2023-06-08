import speech_recognition as sr
import datetime
import pyttsx3
import os
import tkinter as tk
import webbrowser
import urllib.parse
import cv2

# Speech recognition
r = sr.Recognizer()

# Text-to-speech
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        status_label.config(text="Listening...")  # Update status label
        status_label.update()

        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=1, phrase_time_limit=2)
        except sr.WaitTimeoutError:
            return None

    try:
        status_label.config(text="Recognizing...")  # Update status label
        status_label.update()

        command = r.recognize_google(audio)
        command_label.config(text=f"Command: {command}")  # Update command label
        command_label.update()
        return command

    except Exception as e:
        return None

def speak(response):
    engine.say(response)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I Am Droid Your Desktop Assistant , How Can I Help You ?')
    

def open_notepad():
    location = "C:\\Windows\\system32\\notepad.exe"
    os.startfile(location)

def open_google():
    webbrowser.open("https://www.google.com/")

def open_yt():
    webbrowser.open("https://www.youtube.com/")

def open_wiki():
    webbrowser.open("https://www.wikipedia.org/")

def open_fb():
    webbrowser.open("https://www.facebook.com/login/")

def open_file_manager():
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("open .")
    elif os.name == "nt":  # Windows
        os.system("explorer .")

def open_photoshop():
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("open .")
    elif os.name == "nt":  # Windows
        os.system("Photoshop .")

def open_code():
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("open .")
    elif os.name == "nt":  # Windows
        os.system("Code .")

def search_google(query):
    query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def show_about():
    about_text = "DROID Desktop Assistant\n\nVersion: 1.0\nDeveloped by: Ayush Sharma\n\nDROID is an AI-powered virtual assistant designed to perform various tasks on your desktop. It can open applications, browse the web, and respond to voice commands. DROID aims to enhance your productivity and make your daily tasks easier. Enjoy using DROID!"
    speak(about_text)

def exit_program():
    speak("Closing the program. Goodbye!")
    window.quit()

def open_chatgpt():
    webbrowser.open("https://chat.openai.com/")

def open_camera():
    camera_index = 0  # Start with index 0
    camera = None

    while camera_index < 10:  # Try index values up to 10
        camera = cv2.VideoCapture(camera_index)  # Open the camera

        if camera.isOpened():
            break

        camera_index += 1

    if camera is None or not camera.isOpened():
        speak("Failed to open the camera.")
        return

    while True:
        ret, frame = camera.read()  # Capture a frame from the camera

        cv2.imshow("Camera", frame)  # Display the frame in a window

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Check for key press event
            break

    camera.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the window

def shutdown_pc():
    speak("Shutting down the PC")
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("shutdown now")
    elif os.name == "nt":  # Windows
        os.system("shutdown /s /t 0")

def restart_pc():
    speak("Restarting the PC")
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("reboot")
    elif os.name == "nt":  # Windows
        os.system("shutdown /r /t 0")

def sleep_pc():
    speak("Putting the PC to sleep")
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("pmset sleepnow")
    elif os.name == "nt":  # Windows
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def process_command():
    wish()
    while True:
        command = listen()

        if command is None:
            command_label.config(text="Command: Null")  # Update command label
            command_label.update()
            continue

        command = command.lower()

        if "hello" in command:
            speak("Hello! How can I assist you?")

        elif "open camera" in command:
            open_camera()

        elif "open notepad" in command:
            open_notepad()

        elif "open youtube" in command:
            open_yt()

        elif "open browser" in command:
            open_google()

        elif "open wikipedia" in command:
            open_wiki()

        elif "open facebook" in command:
            open_fb()

        elif "open file manager" in command:
            open_file_manager()
        
        elif "open vs code" in command:
            open_code()

        elif "droid please shutdown pc" in command:
            shutdown_pc()

        elif "droid please restart pc" in command:
            restart_pc()

        elif "droid please sleep mode" in command:
            sleep_pc()

        elif "open photoshop" in command:
            open_photoshop()

        elif "search on google" in command:
            speak("What do you want to search for?")
            search_query = listen()
            if search_query:
                search_google(search_query)
            else:
                speak("Sorry, I didn't catch that. Can you please repeat the search query?")

        elif "open chat gpt" in command:
            open_chatgpt()

        elif "about droid" in command:
            show_about()

        elif "goodbye" in command or "exit droid" in command:
            speak("Thanks For Using Droid,Goodbye")
            window.quit()
            break

        else:
            speak("I'm sorry, I didn't understand your command.")
        




#UI CODE 

window = tk.Tk()
window.title("DROID")

# Set window dimensions and position
window.geometry("400x250")
window.resizable(False, False)

# Create a custom font style
font_style = ("Arial", 12, "bold")

# Set background color to black
window.configure(bg="black")

# Create a welcome label
welcome_label = tk.Label(window, text="DROID : DESKTOP ASSISTANT", font=font_style, fg="Yellow", bg="black")
welcome_label.pack(pady=10)

# Create the status label
status_label = tk.Label(window, text="Status: Idle", font=font_style, fg="White", bg="black")
status_label.pack()

# Create the command label
command_label = tk.Label(window, text="Command: ", font=font_style, fg="White", bg="black")
command_label.pack()

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=10)

# Create the "Run" button
run_button = tk.Button(button_frame, text="Run", font=font_style, width=15, command=process_command, relief=tk.RAISED, bd=0)
run_button.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH)

# Create the "About" button
about_button = tk.Button(button_frame, text="About", font=font_style, width=15, command=show_about, relief=tk.RAISED, bd=0)
about_button.pack(side=tk.RIGHT, padx=10, pady=5, fill=tk.BOTH)

# Configure rounded corners for buttons
window.update()
run_button.configure(
    relief=tk.RAISED,
    bd=0,
    highlightthickness=0,
    bg="#555555",
    fg="white",
    activebackground="#777777",
    activeforeground="white",
    cursor="hand2"
)

about_button.configure(
    relief=tk.RAISED,
    bd=0,
    highlightthickness=0,
    bg="#555555",
    fg="white",
    activebackground="#777777",
    activeforeground="white",
    cursor="hand2"
)

# Create the exit instructions label
exit_label = tk.Label(window, text="To Exit Or Close The Application, Say 'Goodbye'", font=font_style, fg="White", bg="black")
exit_label.pack(pady=10)


window.mainloop()

