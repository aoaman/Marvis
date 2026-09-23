import subprocess

MIC_DEVICE = "plughw:2,0"
AUDIO_FILE = "/tmp/marvis_input.wav"

def record_audio(duration=5):
    """Record audio from the USB micrphone"""

    print("Listening....")

    subprocess.run(
        [
        "arecord", # linux program used to record audio from a microphone
        "-D", MIC_DEVICE, # specify the device to record from
        "-f", "S16_LE", # specify the format of the audio file signed 16-bit little-endian
        "-r", "16000", # specify the samplet rate
        "-c", "1", # specifying the number of channels
        "-d", str(duration), # specify the duration of the recorfing in seconds
        AUDIO_FILE, 
        ],

        check=True, # if arecord fails, raise an error instead of continuing the program
    )
    return AUDIO_FILE