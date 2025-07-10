import os
from gtts import gTTS
import subprocess
import platform
from pydub import AudioSegment

def text_to_speech_old(text, output_filepath):
    language="en"
    audioobj=gTTS(
        text=text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hi this is AI with Girban!"
# text_to_speech_old(text=input_text, output_filepath="gtts_test.mp3")

def text_to_speech(text, output_filepath_mp3, output_filepath_wav):
    language="en"
    audioobj=gTTS(
        text=text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath_mp3)

    sound = AudioSegment.from_mp3(output_filepath_mp3)
    sound.export(output_filepath_wav, format="wav")

    os_name=platform.system()
    try:
        if os_name=="Darwin":
            subprocess.run(['afplay', output_filepath_wav])
        elif os_name=="Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath_wav}").PlaySync();'])
        elif os_name=="Linux":
            subprocess.run(['aplay', output_filepath_wav])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An error occured while trying to play the audio : {e}")

input_text="Hi this is AI with Girban!"
text_to_speech(text=input_text, output_filepath_mp3="gtts_test.mp3", output_filepath_wav="gtts_test.wav")