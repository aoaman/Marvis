from app.audio import record_audio

from app.speech import transcribe

def main():
    """Run the the main Marvis assistant program"""

    input("Press ENTER to speak....") # pauses the program until enter is pressed

    audio_file = record_audio() # record audio from the microphone

    text = transcribe(audio_file) # convert the recorded audio to text

    print(f"\nYou said: {text}")

if __name__ == "__main__": # 
    main()



