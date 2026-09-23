import subprocess

WHISPER = "/home/aoajarv/whisper.cpp/build/bin/whisper-cli" # path to the whisper executable

WHISPER_MODEL = "/home/aoajarv/whisper.cpp/models/ggml-base.en.bin" # path to the whisper model

def transcribe(audio_file):
    """convert recorded audion to text using whisper """

    result = subprocess.run(
        [
            WHISPER,

            "-m", WHISPER_MODEL, # specify which model to use

            "-f", audio_file, # specify the audio file to transcribe

            "--no-timestamps", # only want the spoken text returned not the time stamps
        ],

        capture_output=True, # capture the output of the command

        text=True, # return output as string instead of bytes

        check=True, # if whisper fails, raise an error instead of continuing the program
    )

    return result.stdout.strip() # return the transcribed text without any leading or trailing whitespace