import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to sing the song (text-to-speech)
def sing_song():
    song_text = text_entry.get("1.0", "end-1c")  # Get the text from the input box
    engine.say(song_text)  # Speak the text
    engine.runAndWait()  # Wait for the speech to finish

# Function to stop singing
def stop_song():
    engine.stop()  # Stop the text-to-speech engine

# Create the main GUI window
root = tk.Tk()
root.title("Text Song Singer")
root.geometry("400x300")

# Label for instructions
label = tk.Label(root, text="Enter the song lyrics below:")
label.pack(pady=10)

# Text box to enter the song lyrics
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=10)

# Button to start singing
sing_button = tk.Button(root, text="Sing!", command=sing_song, bg="green", fg="white", font=("Arial", 12))
sing_button.pack(pady=5)

# Button to stop singing
stop_button = tk.Button(root, text="Stop", command=stop_song, bg="red", fg="white", font=("Arial", 12))
stop_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
