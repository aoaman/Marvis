from app.audio import record_audio

from app.speech import transcribe

from app.brain import ask_marvis

def main():
    """Run the the main Marvis assistant program"""

    input("Press ENTER to speak....") # pauses the program until enter is pressed

    audio_file = record_audio() # record audio from the microphone

    user_text = transcribe(audio_file) # convert the recorded audio to text

    print(f"\nYou said: {user_text}")

    response = ask_marvis(user_text)

    print(f"\nMarvis: {response}")

if __name__ == "__main__": 
    main()



